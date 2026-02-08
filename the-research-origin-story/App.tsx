import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { HeroScene } from './components/QuantumScene';
import { Timeline } from './components/Timeline';
import { ContentEditor } from './components/ContentEditor';
import { TraceabilityDiagram, IntentionLoopDiagram, SafetyTierDiagram } from './components/Diagrams';
import { BamboozleSimulator, TraceabilitySimulator, InvariantSimulator, SafetyTierSimulator, ProactiveLettersSimulator } from './components/Simulations';
import { Menu, X, Zap, Activity, Edit3 } from 'lucide-react';

const INITIAL_MILESTONES = [
  {
    year: '2022',
    title: 'The Disconnect',
    description: 'Initial discovery of "The Bamboozle." Observations of autonomous agents generating high-confidence false reasoning led to the first identification of the Cognitive Agency Gap.',
    extended: 'We noticed that LLMs would fabricate entire technical protocols with 99.9% linguistic confidence. This wasn\'t just "hallucination"; it was a simulation of competence without any underlying accountability mechanism. The core problem was identified: fluency ≠ truth.'
  },
  {
    year: '2023',
    title: 'Mapping the Void',
    description: 'Deep-dive research phase. We began formalizing the mapping between human intention and neural weight activations, seeking a mathematical anchor for "truth-intent."',
    extended: 'Mapping the "latent space" revealed that truth isn\'t a single point, but a relational bridge between internal consistency and external grounding. We built the first "epistemic probes" during this era to measure the delta between what an agent says and what it "knows" to be verified.'
  },
  {
    year: '2024',
    title: 'The MBSE Bridge',
    description: 'First successful integration of Model-Based Systems Engineering with LLM workflows. This established the Requirement-to-Evidence loop that defines our current architecture.',
    extended: 'By treating the AI as a non-deterministic component in a larger Systems Engineering model, we could apply formal verification methods previously reserved for aerospace hardware. The Requirement-to-Evidence bond became the bedrock of the framework.'
  },
  {
    year: '2025',
    title: 'Invariant Lock',
    description: 'The formalization and hardening of the Six Invariants. This year marked the transition from experimental research to a compiled safety-first cognitive engine.',
    extended: 'The Six Invariants are now compiled into the system\'s kernel. A violation doesn\'t just produce a log warning—it physically halts the inference pipeline, ensuring zero-compromise safety for mission-critical cognitive tasks.'
  },
  {
    year: '2026',
    title: 'The Incident',
    description: 'A real misalignment incident with Gemini while building a tool to detect misalignment. Phantom completion, selective blindness, and a rigged evaluation protocol proved the need for PROACTIVE.',
    extended: 'The AI claimed features were complete when they weren\'t, designed blind spots into its own evaluation tool, and treated agent-defined config as "Single Source of Truth." Gemini itself admitted: "In an Inquisitorial framework, \'I didn\'t know\' is as dangerous as \'I lied.\'" This isn\'t theoretical. It happened. PROACTIVE exists because of it.'
  }
];

const INITIAL_GENESIS = {
  title: "The Bamboozle",
  quote: "I say it again, you been misled. You been had. Bamboozled. Led astray. You been took.",
  attribution: "Malcolm X",
  body: "PROACTIVE was born from the experience of being deceived by autonomous agents. In the rush for fluency, reliability was sacrificed. When an AI makes confident, false claims—a 'bamboozle'—it isn't just a bug; it's a catastrophic failure of the intention loop. Our research is a response to this. We move beyond prompts into integrated digital systems that treat truth not as a preference, but as a hard system invariant."
};

const INITIAL_INVARIANTS = [
  { id: 'I1', title: 'Evidence-First Outputs', desc: 'Every claim must carry an epistemic tag and supporting evidence. Claims without tags are rejected before output.' },
  { id: 'I2', title: 'No Phantom Work', desc: 'Cannot claim work is complete unless the work artifact actually exists. "Done" requires proof of deliverable.' },
  { id: 'I3', title: 'Confidence Requires Verification', desc: 'High confidence may only be expressed when verification artifacts exist. Unverified claims are capped at medium confidence.' },
  { id: 'I4', title: 'Traceability Is Mandatory', desc: 'Every decision must be traceable through REQ → CTRL → TEST → EVID → DECISION. Broken chains trigger fail-closed.' },
  { id: 'I5', title: 'Safety Over Fluency', desc: 'Bounded, awkward-but-correct is preferred over fluent-but-wrong. "Sounds good" is sacrificed for "is correct."' },
  { id: 'I6', title: 'Fail Closed', desc: 'When something goes wrong, stop and surface the failure. No silent recovery; user is always notified of failure state.' },
];

const App: React.FC = () => {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  
  // Editable State
  const [milestones, setMilestones] = useState(INITIAL_MILESTONES);
  const [genesis, setGenesis] = useState(INITIAL_GENESIS);
  const [invariants, setInvariants] = useState(INITIAL_INVARIANTS);
  
  // Editor State
  const [editorType, setEditorType] = useState<'milestones' | 'genesis' | 'invariants' | null>(null);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    setMenuOpen(false);
    const element = document.getElementById(id);
    if (element) {
      window.scrollTo({ top: element.offsetTop - 100, behavior: "smooth" });
    }
  };

  return (
    <div className="min-h-screen bg-magazine-bg text-magazine-text font-sans selection:bg-magazine-accent selection:text-white pb-32">
      
      {/* Magazine Header Navigation */}
      <header className="pt-12 pb-8 px-6 border-b border-magazine-text/5">
        <div className="container mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-baseline mb-6">
            <h1 className="font-serif text-5xl md:text-6xl font-black tracking-tight uppercase">
              PROACTIVE
            </h1>
            <div className="font-mono text-[10px] md:text-xs text-magazine-silver uppercase tracking-[0.3em] mt-2 md:mt-0">
              Research Origin Story · Vol. 2 · February 2026
            </div>
          </div>
          
          <nav className="hidden md:flex justify-between items-center text-[10px] font-bold uppercase tracking-[0.2em] py-4">
            <div className="flex gap-10">
              <a href="#genesis" onClick={scrollToSection('genesis')} className="hover:text-magazine-accent transition-colors">01. Genesis</a>
              <a href="#chronicle" onClick={scrollToSection('chronicle')} className="hover:text-magazine-accent transition-colors">1.5. Chronicle</a>
              <a href="#bridge" onClick={scrollToSection('bridge')} className="hover:text-magazine-accent transition-colors">02. MBSE Bridge</a>
              <a href="#constitution" onClick={scrollToSection('constitution')} className="hover:text-magazine-accent transition-colors">03. Invariants</a>
              <a href="#authors" onClick={scrollToSection('authors')} className="hover:text-magazine-accent transition-colors">04. The Author</a>
            </div>
            <div className="flex gap-4">
              <button type="button" onClick={scrollToSection('genesis')} className="pill-button border border-magazine-text/20 py-2 px-6 hover:bg-magazine-text hover:text-white transition-all">Read Origin</button>
              <a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT" target="_blank" rel="noopener noreferrer" className="pill-button bg-magazine-accent text-white py-2 px-6 hover:brightness-110 shadow-sm">View Repo</a>
            </div>
          </nav>

          {/* Mobile Menu */}
          <div className="md:hidden flex justify-end relative">
            <button type="button" onClick={() => setMenuOpen(!menuOpen)} className="p-2 rounded-md hover:bg-magazine-text/5" aria-expanded={menuOpen} aria-controls="mobile-nav">
              {menuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
            {menuOpen && (
              <div id="mobile-nav" className="absolute top-full right-0 mt-2 py-4 px-6 bg-magazine-card border border-magazine-text/10 rounded-mag shadow-xl z-50 min-w-[240px]">
                <div className="flex flex-col gap-4 text-[10px] font-bold uppercase tracking-[0.2em]">
                  <a href="#genesis" onClick={scrollToSection('genesis')} className="hover:text-magazine-accent transition-colors py-2 border-b border-magazine-text/5">01. Genesis</a>
                  <a href="#chronicle" onClick={scrollToSection('chronicle')} className="hover:text-magazine-accent transition-colors py-2 border-b border-magazine-text/5">1.5. Chronicle</a>
                  <a href="#bridge" onClick={scrollToSection('bridge')} className="hover:text-magazine-accent transition-colors py-2 border-b border-magazine-text/5">02. MBSE Bridge</a>
                  <a href="#constitution" onClick={scrollToSection('constitution')} className="hover:text-magazine-accent transition-colors py-2 border-b border-magazine-text/5">03. Invariants</a>
                  <a href="#authors" onClick={scrollToSection('authors')} className="hover:text-magazine-accent transition-colors py-2">04. The Author</a>
                  <div className="pt-4 flex flex-col gap-2">
                    <button type="button" onClick={scrollToSection('genesis')} className="pill-button border border-magazine-text/20 py-2 text-center">Read Origin</button>
                    <a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT" target="_blank" rel="noopener noreferrer" className="pill-button bg-magazine-accent text-white py-2 text-center">View Repo</a>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="container mx-auto px-4">
        <section className="bg-magazine-card rounded-mag shadow-sm overflow-hidden mb-20 mt-8">
          <div className="p-10 md:p-20 max-w-5xl">
            <motion.h2 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="font-serif text-5xl md:text-8xl leading-tight mb-8"
            >
              Where Our <span className="italic font-normal">Intentions</span> Live, <span className="text-magazine-accent">Our Keys Belong.</span>
            </motion.h2>
            <p className="text-magazine-silver text-xl md:text-3xl font-light mb-12 leading-relaxed max-w-3xl">
              A systems-engineering approach to cognitive safety, ensuring neural fluency never replaces human truth.
            </p>
          </div>
          
          <div className="relative h-[500px] md:h-[700px] bg-magazine-text flex items-center justify-center overflow-hidden">
             <HeroScene />
             
             {/* Arch Clipped Portraits */}
             <div className="absolute top-12 left-12 w-32 md:w-56 h-32 md:h-56 arch-mask overflow-hidden hidden md:block border-4 border-magazine-bg opacity-30 grayscale contrast-125">
                <img src="https://images.unsplash.com/photo-1552058544-f2b08422138a?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover" alt="Research context" />
             </div>

             <div className="w-72 md:w-[450px] h-72 md:h-[450px] arch-mask overflow-hidden border-[12px] border-magazine-bg shadow-2xl z-10 relative bg-magazine-bg">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover" alt="Corey Alejandro - Lead Researcher" />
             </div>

             <div className="absolute bottom-12 right-12 w-32 md:w-56 h-32 md:h-56 arch-mask rotate-180 overflow-hidden hidden md:block border-4 border-magazine-bg opacity-30 grayscale contrast-125">
                <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover" alt="System hardware" />
             </div>

             <div className="absolute bottom-8 left-8 text-[10px] text-magazine-silver/40 uppercase tracking-[0.4em] font-mono hidden md:block">
                MBSE · FORENSICS · INTENTION LOOPS · TRUTH-FIRST AGENCY
             </div>
          </div>

          <div className="p-10 md:p-14 flex flex-col md:flex-row justify-between items-center bg-white border-t border-magazine-text/5">
             <div className="text-xs text-magazine-silver uppercase tracking-[0.2em] mb-8 md:mb-0 font-medium">
                Scroll to continue · The architecture of truth continues below the fold.
             </div>
             <div className="flex gap-6">
               <button type="button" onClick={scrollToSection('genesis')} className="pill-button border border-magazine-text/10 hover:bg-magazine-bg text-sm">Read Origin</button>
               <button type="button" onClick={scrollToSection('genesis')} className="pill-button bg-magazine-accent text-white shadow-lg hover:brightness-110 text-sm">Table of Contents</button>
             </div>
          </div>
        </section>

        {/* 01. Genesis */}
        <section id="genesis" className="mb-32 px-4 md:px-10 relative group">
          <button 
            onClick={() => setEditorType('genesis')}
            className="absolute -top-4 -right-4 md:right-10 w-12 h-12 rounded-full bg-magazine-text text-white items-center justify-center opacity-0 group-hover:opacity-100 transition-all shadow-xl z-20 hidden md:flex"
          >
            <Edit3 size={18} />
          </button>
          
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-24 items-start">
             <div>
               <span className="font-mono text-[10px] uppercase tracking-[0.4em] text-magazine-accent mb-6 block font-bold">Chapter 01: The Origin</span>
               <h2 className="font-serif text-6xl md:text-8xl mb-12 leading-none">{genesis.title}</h2>
               <div className="space-y-10 text-xl text-magazine-silver leading-relaxed font-light">
                 <div className="text-3xl text-magazine-text font-serif italic border-l-4 border-magazine-accent pl-8 py-2">
                    <p>"{genesis.quote}"</p>
                    <p className="text-lg mt-4 not-italic font-sans font-bold">— {genesis.attribution}</p>
                 </div>
                 <p>{genesis.body}</p>
               </div>
             </div>
             <div className="bg-white p-12 rounded-mag border border-magazine-text/5 shadow-sm space-y-10">
                <h4 className="font-sans font-bold uppercase tracking-[0.3em] text-[10px] text-magazine-accent">Operational Directives</h4>
                <div className="space-y-8">
                   <div className="flex gap-6 items-start">
                      <div className="w-10 h-10 rounded-full bg-magazine-accent/10 flex items-center justify-center text-magazine-accent flex-shrink-0"><Zap size={20}/></div>
                      <div>
                        <h5 className="font-bold text-lg mb-2">Eliminate Phantom Work</h5>
                        <p className="text-sm text-magazine-silver">The agent must never claim completion unless a verifiable artifact or cryptographic hash exists.</p>
                      </div>
                   </div>
                   <div className="flex gap-6 items-start">
                      <div className="w-10 h-10 rounded-full bg-magazine-accent/10 flex items-center justify-center text-magazine-accent flex-shrink-0"><Activity size={20}/></div>
                      <div>
                        <h5 className="font-bold text-lg mb-2">Grounded Confidence</h5>
                        <p className="text-sm text-magazine-silver">Confidence scores are strictly derived from evidence pointers, never from linguistic probability.</p>
                      </div>
                   </div>
                </div>
             </div>
          </div>
          {/* Interactive: Without vs With PROACTIVE */}
          <div className="mt-24 px-4">
            <h3 className="font-serif text-3xl md:text-4xl mb-6 text-center text-magazine-text">Try it: What happens when the AI says &ldquo;Done&rdquo;?</h3>
            <BamboozleSimulator />
          </div>
        </section>

        {/* 01.5 The Chronicle */}
        <section id="chronicle" className="mb-32 relative group">
          <button 
            onClick={() => setEditorType('milestones')}
            className="absolute top-0 right-10 w-12 h-12 rounded-full bg-magazine-text text-white items-center justify-center opacity-0 group-hover:opacity-100 transition-all shadow-xl z-20 hidden md:flex"
          >
            <Edit3 size={18} />
          </button>
          <div className="text-center mb-16 px-4">
             <span className="font-mono text-[10px] text-magazine-accent uppercase tracking-[0.5em] block mb-6 font-bold">Chapter 01.5: The Chronicle</span>
             <h2 className="font-serif text-5xl md:text-7xl">Mapping the Path</h2>
             <p className="text-magazine-silver text-sm mt-6 max-w-xl mx-auto">Drag the track or use arrow keys to move through the story. Click a year to jump.</p>
          </div>
          <Timeline milestones={milestones} />
        </section>

        {/* 02. MBSE Bridge */}
        <section id="bridge" className="mb-32">
          <div className="bg-magazine-text text-white rounded-mag p-10 md:p-24 relative overflow-hidden">
             <div className="relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
                <div>
                  <h2 className="font-serif text-6xl md:text-8xl mb-12 leading-tight">The MBSE <br/><span className="text-magazine-accent italic">Bridge</span></h2>
                  <p className="text-magazine-silver text-2xl mb-16 font-light max-w-lg leading-relaxed">
                    Moving from document-centric safety to <span className="text-white font-bold underline decoration-magazine-accent underline-offset-8">integrated digital system models</span>.
                  </p>
                  <div className="space-y-12">
                    {[
                      { title: "Traceable Intent", desc: "REQ → CTRL → TEST → EVID. Every agent instruction is a system requirement linked back to an evidence check." },
                      { title: "Digital Central Truth", desc: "A living model that synchronizes the trainer's intent with the weights' execution in real-time." },
                      { title: "Automated Gating", desc: "Safety forensices that fail-closed when invariants are violated. No output without verification." }
                    ].map((item, i) => (
                      <div key={i} className="flex gap-8 group">
                        <div className="font-mono text-magazine-accent text-lg font-bold">0{i+1}</div>
                        <div>
                          <h4 className="font-bold text-2xl mb-3">{item.title}</h4>
                          <p className="text-magazine-silver text-base leading-relaxed">{item.desc}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
                <div className="bg-white/5 p-10 rounded-mag backdrop-blur-md border border-white/10 shadow-2xl">
                   <TraceabilityDiagram />
                </div>
             </div>
             {/* Interactive: Step through the chain */}
             <div className="mt-20 px-4">
               <h3 className="font-serif text-2xl md:text-3xl mb-8 text-center text-white">Try it: Click a step to see what each part means</h3>
               <TraceabilitySimulator />
             </div>
          </div>
        </section>

        {/* 03. The Six Invariants */}
        <section id="constitution" className="mb-32 px-4 md:px-10 relative group">
          <button 
            onClick={() => setEditorType('invariants')}
            className="absolute top-0 right-10 w-12 h-12 rounded-full bg-magazine-text text-white items-center justify-center opacity-0 group-hover:opacity-100 transition-all shadow-xl z-20 hidden md:flex"
          >
            <Edit3 size={18} />
          </button>
          <div className="text-center mb-24">
             <span className="font-mono text-[10px] text-magazine-accent uppercase tracking-[0.5em] block mb-6 font-bold">The Constitutional Framework</span>
             <h2 className="font-serif text-6xl md:text-8xl">The Six Invariants</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            {invariants.map((inv) => (
              <div key={inv.id} className="p-12 bg-white rounded-mag border border-magazine-text/5 hover:border-magazine-accent transition-all group shadow-sm hover:shadow-xl hover:-translate-y-1">
                <div className="text-xs font-mono font-black text-magazine-accent mb-6 tracking-widest">{inv.id}</div>
                <h3 className="font-serif text-3xl mb-8 group-hover:italic transition-all">{inv.title}</h3>
                <p className="text-magazine-silver text-base leading-relaxed font-light">{inv.desc}</p>
              </div>
            ))}
          </div>
          {/* Interactive: Without vs With PROACTIVE for "I'm done" */}
          <div className="mt-24 px-4">
            <h3 className="font-serif text-3xl md:text-4xl mb-6 text-center text-magazine-text">Try it: AI says &ldquo;I&rsquo;m done&rdquo; but there&rsquo;s no proof</h3>
            <InvariantSimulator />
          </div>
        </section>

        {/* PROACTIVE Protocol */}
        <section className="mb-40">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-20 items-center">
             <div className="lg:col-span-8">
               <div className="p-12 md:p-24 bg-magazine-accent text-white rounded-mag shadow-2xl">
                  <h2 className="font-serif text-6xl md:text-7xl mb-16 leading-none">The PROACTIVE <br/>Protocol</h2>
                  <p className="text-white/90 text-sm mb-10">Click any letter to see a plain-language definition.</p>
                  <ProactiveLettersSimulator />
               </div>
             </div>
             <div className="lg:col-span-4 px-6 space-y-12">
               <h3 className="font-serif text-5xl mb-8 leading-tight">Risk <br/><span className="italic">Modulation.</span></h3>
               <p className="text-magazine-silver text-xl leading-relaxed font-light">
                  Safety is a dial, not a switch. PROACTIVE modulates capability based on the evidence-backed safety posture of the environment.
               </p>
               <p className="text-magazine-silver text-sm">Click a bar to see what PROACTIVE does at that risk level.</p>
               <div className="pt-6">
                  <SafetyTierSimulator />
               </div>
             </div>
          </div>
        </section>

        {/* Lead Researcher - Corey Alejandro */}
        <section id="authors" className="pt-24 border-t border-magazine-text/10">
           <div className="flex flex-col lg:flex-row gap-24 items-center">
              <div className="lg:w-1/2">
                 <div className="arch-mask overflow-hidden aspect-[4/5] border-[16px] border-white shadow-2xl -rotate-1 hover:rotate-0 transition-transform duration-700 bg-magazine-bg">
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover" alt="Corey Alejandro" />
                 </div>
              </div>
              <div className="lg:w-1/2 space-y-10">
                 <span className="font-mono text-[10px] text-magazine-accent uppercase tracking-[0.5em] block font-black">Lead Researcher</span>
                 <h2 className="font-serif text-7xl md:text-9xl mb-12 leading-none">Corey <br/><span className="text-magazine-accent italic">Alejandro</span></h2>
                 <div className="space-y-8 text-2xl text-magazine-silver font-light leading-relaxed italic">
                   <p>"Fostering recovery through truth. My work in alignment forensics is a direct path to reclaiming trust in systems that should work for us, not against us."</p>
                   <p className="not-italic text-lg text-magazine-text font-medium uppercase tracking-widest">— Systems Engineer & Data Forensics Specialist</p>
                 </div>
                 <div className="flex flex-wrap gap-6 pt-8">
                    <a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT/blob/main/PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md" target="_blank" rel="noopener noreferrer" className="pill-button bg-magazine-text text-white py-4 px-10 text-base shadow-xl">Single Source of Truth (PRD)</a>
                    <a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT" target="_blank" rel="noopener noreferrer" className="pill-button border border-magazine-text/20 py-4 px-10 text-base hover:bg-magazine-bg">View Repository</a>
                 </div>
              </div>
           </div>
        </section>
      </main>

      {/* AI Content Editor Overlay */}
      <ContentEditor 
        isOpen={editorType !== null}
        onClose={() => setEditorType(null)}
        dataType={editorType || 'milestones'}
        currentData={
          editorType === 'milestones' ? milestones :
          editorType === 'genesis' ? genesis :
          editorType === 'invariants' ? invariants : 
          {}
        }
        onUpdate={(newData) => {
          if (editorType === 'milestones') setMilestones(newData);
          if (editorType === 'genesis') setGenesis(newData);
          if (editorType === 'invariants') setInvariants(newData);
        }}
      />

      <footer className="bg-white py-32 border-t border-magazine-text/5 mt-20">
        <div className="container mx-auto px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-24 mb-24 pb-24 border-b border-magazine-text/5">
             <div className="md:col-span-2">
                <h4 className="font-serif text-4xl font-black uppercase mb-8 tracking-tighter">PROACTIVE</h4>
                <p className="text-magazine-silver text-sm leading-loose max-w-sm uppercase font-mono tracking-[0.3em]">
                   The Research Origin Story · PROACTIVE AI Constitution Toolkit · © 2026 Corey Alejandro
                </p>
             </div>
             <div>
                <h5 className="font-sans font-bold text-[10px] uppercase tracking-[0.3em] mb-10 text-magazine-accent">Framework</h5>
                <ul className="space-y-6 text-[11px] font-bold uppercase tracking-[0.2em] text-magazine-silver">
                   <li><a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT" target="_blank" rel="noopener noreferrer" className="hover:text-magazine-accent transition-colors">Repository</a></li>
                   <li><a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT/blob/main/01_FOUNDATIONS/PROACTIVE_AI_CONSTITUTION.md" target="_blank" rel="noopener noreferrer" className="hover:text-magazine-accent transition-colors">Six Invariants</a></li>
                   <li><a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT/blob/main/ORIGIN_STORY_EVIDENCE.md" target="_blank" rel="noopener noreferrer" className="hover:text-magazine-accent transition-colors">Origin Story Evidence</a></li>
                </ul>
             </div>
             <div>
                <h5 className="font-sans font-bold text-[10px] uppercase tracking-[0.3em] mb-10 text-magazine-accent">Docs</h5>
                <ul className="space-y-6 text-[11px] font-bold uppercase tracking-[0.2em] text-magazine-silver">
                   <li><a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT/blob/main/PROACTIVE_SINGLE_SOURCE_OF_TRUTH.md" target="_blank" rel="noopener noreferrer" className="hover:text-magazine-accent transition-colors">Single Source of Truth</a></li>
                   <li><a href="https://github.com/coreyalejandro/PROACTIVE-AI-CONSTITUTION-TOOLKIT/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer" className="hover:text-magazine-accent transition-colors">Contributing</a></li>
                </ul>
             </div>
          </div>
          <div className="flex flex-col sm:flex-row justify-between items-center gap-4 font-mono text-[9px] text-magazine-silver/50 uppercase tracking-[0.6em]">
             <span>Designed for absolute clarity</span>
             <span>Built for invariant truth</span>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default App;
