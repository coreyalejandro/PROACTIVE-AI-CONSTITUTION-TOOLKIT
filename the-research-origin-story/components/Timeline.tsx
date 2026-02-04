import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronDown, ChevronUp, MousePointer2 } from 'lucide-react';

interface Milestone {
  year: string;
  title: string;
  description: string;
  extended: string;
}

interface TimelineProps {
  milestones: Milestone[];
}

export const Timeline: React.FC<TimelineProps> = ({ milestones }) => {
  const [activeTab, setActiveTab] = useState(0);
  const [isExpanded, setIsExpanded] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const nodesRef = useRef<(HTMLButtonElement | null)[]>([]);

  // Safety check if milestones change size
  useEffect(() => {
    if (activeTab >= milestones.length) {
      setActiveTab(0);
    }
  }, [milestones]);

  const handleScrub = (clientX: number) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    const x = Math.max(0, Math.min(clientX - rect.left, rect.width));
    const percentage = x / rect.width;
    const closestIndex = Math.round(percentage * (milestones.length - 1));
    if (closestIndex !== activeTab) {
      setActiveTab(closestIndex);
    }
  };

  const onMouseDown = (e: React.MouseEvent) => {
    setIsDragging(true);
    handleScrub(e.clientX);
  };

  const handleNodeClick = (index: number) => {
    setActiveTab(index);
    setIsExpanded(true);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowRight') {
      setActiveTab((prev) => Math.min(prev + 1, milestones.length - 1));
    } else if (e.key === 'ArrowLeft') {
      setActiveTab((prev) => Math.max(prev - 1, 0));
    }
  };

  useEffect(() => {
    const onMouseMove = (e: MouseEvent) => {
      if (isDragging) handleScrub(e.clientX);
    };
    const onMouseUp = () => setIsDragging(false);

    if (isDragging) {
      window.addEventListener('mousemove', onMouseMove);
      window.addEventListener('mouseup', onMouseUp);
    }
    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      window.removeEventListener('mouseup', onMouseUp);
    };
  }, [isDragging]);

  return (
    <div className="w-full py-20 px-4">
      {/* Interactive Scrubbing Track */}
      <div 
        ref={containerRef}
        className="relative mb-32 h-20 flex items-center cursor-crosshair group select-none"
        onMouseDown={onMouseDown}
        role="slider"
        aria-valuemin={0}
        aria-valuemax={milestones.length - 1}
        aria-valuenow={activeTab}
        aria-valuetext={`${milestones[activeTab]?.year}: ${milestones[activeTab]?.title}`}
        aria-label="Narrative timeline scrubber"
        tabIndex={0}
        onKeyDown={handleKeyDown}
      >
        {/* The Track Line */}
        <div className="absolute top-1/2 left-0 w-full h-[1px] bg-magazine-text/10 -translate-y-1/2 group-hover:h-[2px] transition-all" />
        
        {/* Active Progress Bar (Track) */}
        <motion.div 
          className="absolute top-1/2 left-0 h-[2px] bg-magazine-accent -translate-y-1/2"
          initial={false}
          animate={{ width: `${(activeTab / (milestones.length - 1)) * 100}%` }}
          transition={{ type: "spring", stiffness: 300, damping: 30 }}
        />

        {/* Milestone Snap Nodes */}
        <div className="relative flex justify-between items-center w-full" role="tablist">
          {milestones.map((milestone, index) => (
            <button 
              key={milestone.year + index}
              ref={el => nodesRef.current[index] = el}
              id={`tab-${index}`}
              role="tab"
              aria-selected={activeTab === index}
              aria-controls={`panel-${index}`}
              aria-label={`Go to ${milestone.year} milestone: ${milestone.title}`}
              className="relative z-10 focus:outline-none group/node"
              onClick={(e) => {
                e.stopPropagation();
                handleNodeClick(index);
              }}
              tabIndex={-1}
            >
              {/* Year Label */}
              <motion.span 
                animate={{ 
                  color: activeTab === index ? '#D97373' : 'rgba(32, 32, 32, 0.5)',
                  scale: activeTab === index ? 1.2 : 1,
                  y: activeTab === index ? -5 : 0
                }}
                className={`absolute -top-14 left-1/2 -translate-x-1/2 font-serif text-2xl font-bold whitespace-nowrap group-hover/node:text-magazine-accent transition-colors`}
              >
                {milestone.year}
              </motion.span>

              {/* Node Marker */}
              <motion.div 
                animate={{
                  scale: activeTab === index ? 1.5 : 1,
                  backgroundColor: activeTab === index ? '#D97373' : '#F2ECE4',
                  borderColor: activeTab === index ? '#D97373' : 'rgba(32, 32, 32, 0.3)'
                }}
                whileHover={{ scale: 1.6 }}
                whileTap={{ scale: 0.9 }}
                className={`w-3 h-3 rounded-full border-2 shadow-sm transition-all duration-300 ${
                  activeTab === index 
                    ? 'shadow-[0_0_15px_rgba(217,115,115,0.5)]' 
                    : ''
                }`}
              />
            </button>
          ))}
        </div>

        {/* Floating Tooltip hint */}
        {!isDragging && (
          <div className="absolute -bottom-10 left-1/2 -translate-x-1/2 flex items-center gap-2 text-[8px] font-black uppercase tracking-[0.4em] text-magazine-silver/60 opacity-0 group-hover:opacity-100 transition-opacity">
            <MousePointer2 size={10} /> Use Arrows or Drag to Scrub
          </div>
        )}
      </div>

      {/* Narrative Content */}
      <div 
        className="max-w-4xl mx-auto min-h-[450px] relative focus:outline-none"
        aria-live="polite"
        role="region"
      >
        {/* Persistent In-Description Progress Indicator */}
        <div className="flex flex-col items-center mb-10 space-y-3" aria-hidden="true">
          <div className="flex justify-between w-full max-w-[240px] text-[9px] font-black uppercase tracking-[0.3em] text-magazine-silver/70">
            <span className="text-magazine-accent">Milestone 0{activeTab + 1}</span>
            <span>Total 0{milestones.length}</span>
          </div>
          <div className="w-full max-w-[240px] h-[1px] bg-magazine-text/10 overflow-hidden relative">
            <motion.div 
              className="absolute top-0 left-0 h-full bg-magazine-accent"
              initial={false}
              animate={{ width: `${((activeTab + 1) / milestones.length) * 100}%` }}
              transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
            />
          </div>
        </div>

        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab + (milestones[activeTab]?.title || '')}
            id={`panel-${activeTab}`}
            role="tabpanel"
            aria-labelledby={`tab-${activeTab}`}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className="text-center"
          >
            <span className="font-mono text-[10px] uppercase tracking-[0.5em] text-magazine-accent mb-6 block font-black">
              Research Log // Epoch {activeTab + 1}
            </span>
            <h3 className="font-serif text-5xl md:text-8xl mb-10 leading-none">
              {milestones[activeTab]?.title}
            </h3>
            
            <div className="space-y-8">
              <p className="text-xl md:text-3xl text-magazine-text/80 font-light leading-relaxed max-w-3xl mx-auto">
                {milestones[activeTab]?.description}
              </p>

              {/* Expandable Section */}
              <div className="pt-4">
                <button 
                  onClick={() => setIsExpanded(!isExpanded)}
                  aria-expanded={isExpanded}
                  aria-controls={`extended-panel-${activeTab}`}
                  className="inline-flex items-center gap-3 text-[10px] font-bold uppercase tracking-[0.3em] text-magazine-text hover:text-magazine-accent transition-colors group focus:ring-2 focus:ring-magazine-accent focus:ring-offset-4 rounded-sm outline-none"
                >
                  <span className="w-8 h-[1px] bg-magazine-text/20 group-hover:bg-magazine-accent" />
                  {isExpanded ? 'Collapse Research Notes' : 'Expand Research Notes'}
                  {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                </button>

                <motion.div
                  id={`extended-panel-${activeTab}`}
                  initial={false}
                  animate={{ 
                    height: isExpanded ? 'auto' : 0, 
                    opacity: isExpanded ? 1 : 0,
                    marginTop: isExpanded ? '2rem' : '0' 
                  }}
                  transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                  className="overflow-hidden"
                >
                  <div className="p-10 bg-white rounded-mag border border-magazine-text/5 text-left shadow-inner">
                    <p className="text-lg text-magazine-text/70 leading-loose font-serif italic border-l-2 border-magazine-accent pl-8">
                      {milestones[activeTab]?.extended}
                    </p>
                  </div>
                </motion.div>
              </div>
            </div>
          </motion.div>
        </AnimatePresence>
      </div>

      <div className="mt-20 flex justify-center gap-12 text-[9px] font-black uppercase tracking-[0.4em] text-magazine-silver/40 border-t border-magazine-text/5 pt-10">
        <div className="flex items-center gap-3">
          <div className="w-1.5 h-1.5 rounded-full bg-magazine-accent/30" />
          Internal_Chronicle_State: Read
        </div>
        <div className="flex items-center gap-3">
          <div className="w-1.5 h-1.5 rounded-full bg-magazine-accent/30" />
          Sequential_Access_Level: Forensic
        </div>
      </div>
    </div>
  );
};
