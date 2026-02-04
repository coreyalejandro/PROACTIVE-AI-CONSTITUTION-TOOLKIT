
import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Search, ShieldAlert, Layers, FileText, CheckCircle, ArrowRight, Zap, Target } from 'lucide-react';

export const TraceabilityDiagram: React.FC = () => {
  const [active, setActive] = useState(0);
  
  const nodes = [
    { label: 'REQ', icon: <FileText size={24}/> },
    { label: 'CTRL', icon: <Layers size={24}/> },
    { label: 'TEST', icon: <Search size={24}/> },
    { label: 'EVID', icon: <CheckCircle size={24}/> },
    { label: 'DECISION', icon: <ShieldAlert size={24}/> }
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setActive(prev => (prev + 1) % nodes.length);
    }, 2500);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="relative p-10 flex flex-col items-center justify-center gap-12">
      <div className="flex flex-wrap md:flex-nowrap gap-4 items-center justify-center w-full">
        {nodes.map((node, i) => (
          <React.Fragment key={i}>
            <div className="flex flex-col items-center gap-4">
              <motion.div 
                className={`w-16 h-16 rounded-full flex items-center justify-center transition-all duration-500 border-2 ${active === i ? 'bg-magazine-accent border-magazine-accent text-white shadow-lg scale-110' : 'bg-transparent border-white/20 text-white/40'}`}
              >
                {node.icon}
              </motion.div>
              <span className={`text-[10px] font-bold tracking-widest uppercase ${active === i ? 'text-magazine-accent' : 'text-white/20'}`}>{node.label}</span>
            </div>
            {i < nodes.length - 1 && (
              <div className={`hidden md:block w-8 h-[1px] ${active > i ? 'bg-magazine-accent' : 'bg-white/10'} self-center mb-6`}></div>
            )}
          </React.Fragment>
        ))}
      </div>
      <div className="text-center font-mono text-[10px] text-white/30 uppercase tracking-[0.3em]">
        Status: Live_Trace_Verification_Active
      </div>
    </div>
  );
};

export const IntentionLoopDiagram: React.FC = () => {
  return (
    <div className="flex items-center justify-center w-full h-full relative p-12">
      <div className="relative w-64 h-64 md:w-80 md:h-80">
        {/* Soft Circular Path */}
        <div className="absolute inset-0 border-2 border-magazine-text/5 rounded-full"></div>
        
        {/* Orbiting Points */}
        <motion.div 
          className="absolute inset-0"
          animate={{ rotate: 360 }}
          transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
        >
          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3 h-3 bg-magazine-accent rounded-full shadow-[0_0_10px_#D97373]"></div>
        </motion.div>

        {/* The 4 Phases */}
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="w-40 h-40 bg-magazine-bg border-4 border-magazine-accent rounded-full flex flex-col items-center justify-center text-center p-4 shadow-xl">
             <Zap size={32} className="text-magazine-accent mb-2" />
             <span className="font-serif italic text-xl font-bold leading-none">Intention<br/>Core</span>
          </div>
        </div>

        {/* Phase Labels */}
        <div className="absolute -top-6 left-1/2 -translate-x-1/2 text-[10px] font-bold uppercase tracking-widest">Capture</div>
        <div className="absolute top-1/2 -right-12 -translate-y-1/2 text-[10px] font-bold uppercase tracking-widest rotate-90">Validate</div>
        <div className="absolute -bottom-6 left-1/2 -translate-x-1/2 text-[10px] font-bold uppercase tracking-widest">Translate</div>
        <div className="absolute top-1/2 -left-12 -translate-y-1/2 text-[10px] font-bold uppercase tracking-widest -rotate-90">Feedback</div>
      </div>
    </div>
  );
};

export const SafetyTierDiagram: React.FC = () => {
  const tiers = [
    { label: 'Blocked', h: 'h-1/5', c: 'bg-magazine-text' },
    { label: 'Escalated', h: 'h-2/5', c: 'bg-magazine-silver' },
    { label: 'Constrained', h: 'h-3/5', c: 'bg-magazine-accent/50' },
    { label: 'Monitored', h: 'h-4/5', c: 'bg-magazine-accent/80' },
    { label: 'Harmless', h: 'h-full', c: 'bg-magazine-accent' },
  ];

  return (
    <div className="flex gap-4 items-end h-48 w-full mt-6">
      {tiers.map((tier, i) => (
        <div key={i} className="flex-1 flex flex-col gap-3 items-center group">
          <motion.div 
            className={`w-full ${tier.c} rounded-t-xl transition-all relative overflow-hidden`}
            initial={{ height: 0 }}
            animate={{ height: tier.h.replace('h-', '') }}
            transition={{ duration: 1, delay: i * 0.1 }}
          >
             <div className="absolute top-2 left-0 w-full text-center text-[8px] text-white opacity-40 font-bold uppercase">LVL_{i+1}</div>
          </motion.div>
          <span className="text-[8px] font-bold uppercase tracking-widest text-magazine-silver group-hover:text-magazine-accent transition-colors">{tier.label}</span>
        </div>
      ))}
    </div>
  );
};
