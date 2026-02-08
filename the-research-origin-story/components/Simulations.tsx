/**
 * Interactive simulations for the research visualization.
 * Written so anyone can understand: simple diagrams, plain language, click-to-reveal.
 */

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { AlertTriangle, CheckCircle2, XCircle, ArrowRight, FileText, Layers, Search, CheckCircle, ShieldAlert, Play, Hand, Zap } from 'lucide-react';

// ——— 1. The Bamboozle Simulator (Genesis) ———
const BAMBOOZLE_STEPS_WITHOUT = [
  { icon: Hand, text: 'You ask the AI to do something' },
  { icon: Zap, text: 'AI says "Done!"' },
  { icon: XCircle, text: 'No proof it actually did it' },
  { icon: AlertTriangle, text: 'You trust it and act — and get hurt' },
];
const BAMBOOZLE_STEPS_WITH = [
  { icon: Hand, text: 'You ask the AI to do something' },
  { icon: Zap, text: 'AI says "Done!"' },
  { icon: Search, text: 'PROACTIVE checks: is there proof?' },
  { icon: XCircle, text: 'No artifact found' },
  { icon: ShieldAlert, text: 'Blocked. You get the truth instead of a confident lie.' },
];

export const BamboozleSimulator: React.FC = () => {
  const [activeFlow, setActiveFlow] = useState<'without' | 'with'>('without');
  const [step, setStep] = useState(0);
  const steps = activeFlow === 'without' ? BAMBOOZLE_STEPS_WITHOUT : BAMBOOZLE_STEPS_WITH;
  const maxStep = steps.length - 1;

  const advance = () => setStep((s) => (s >= maxStep ? 0 : s + 1));
  const reset = (flow: 'without' | 'with') => {
    setActiveFlow(flow);
    setStep(0);
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6 md:p-10 bg-white rounded-mag border border-magazine-text/10 shadow-sm">
      <p className="text-center text-magazine-silver text-sm mb-6 font-medium">
        See what happens when an AI says "Done" but didn't actually do it
      </p>
      <div className="flex gap-4 justify-center mb-8">
        <button
          type="button"
          onClick={() => reset('without')}
          className={`pill-button py-2 px-6 text-sm font-bold uppercase tracking-wider transition-all ${
            activeFlow === 'without' ? 'bg-magazine-text text-white' : 'border border-magazine-text/20 hover:bg-magazine-bg'
          }`}
        >
          Without PROACTIVE
        </button>
        <button
          type="button"
          onClick={() => reset('with')}
          className={`pill-button py-2 px-6 text-sm font-bold uppercase tracking-wider transition-all ${
            activeFlow === 'with' ? 'bg-magazine-accent text-white' : 'border border-magazine-text/20 hover:bg-magazine-bg'
          }`}
        >
          With PROACTIVE
        </button>
      </div>
      <div className="flex flex-col items-center gap-6">
        {steps.map((s, i) => {
          const Icon = s.icon;
          const isActive = i === step;
          const isPast = i < step;
          return (
            <motion.div
              key={`${activeFlow}-${i}`}
              initial={false}
              animate={{
                opacity: isActive ? 1 : isPast ? 0.7 : 0.35,
                scale: isActive ? 1.02 : 1,
              }}
              className={`flex items-center gap-4 w-full max-w-md px-4 py-3 rounded-xl border-2 transition-colors ${
                isActive ? 'border-magazine-accent bg-magazine-accent/5' : 'border-magazine-text/10 bg-magazine-bg/30'
              }`}
            >
              <div className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
                activeFlow === 'with' && i === steps.length - 1 ? 'bg-magazine-accent text-white' : isActive ? 'bg-magazine-accent/20 text-magazine-accent' : 'bg-magazine-text/10 text-magazine-silver'
              }`}>
                <Icon size={20} />
              </div>
              <span className={`text-sm md:text-base font-medium ${isActive ? 'text-magazine-text' : 'text-magazine-silver'}`}>
                {s.text}
              </span>
            </motion.div>
          );
        })}
      </div>
      <div className="flex justify-center mt-8">
        <button
          type="button"
          onClick={advance}
          className="pill-button bg-magazine-text text-white py-2 px-8 flex items-center gap-2 text-sm font-bold uppercase tracking-wider hover:brightness-110"
        >
          <Play size={16} />
          {step >= maxStep ? 'Replay' : 'Next step'}
        </button>
      </div>
    </div>
  );
};

// ——— 2. Traceability Simulator (MBSE Bridge) ———
const TRACE_NODES = [
  { label: 'REQ', short: 'What you asked for', icon: FileText },
  { label: 'CTRL', short: 'How we’ll do it', icon: Layers },
  { label: 'TEST', short: 'Did it work?', icon: Search },
  { label: 'EVID', short: 'Proof', icon: CheckCircle },
  { label: 'DECISION', short: 'Allow or block', icon: ShieldAlert },
];

export const TraceabilitySimulator: React.FC = () => {
  const [step, setStep] = useState(0);
  const maxStep = TRACE_NODES.length - 1;

  return (
    <div className="relative p-6 md:p-10 flex flex-col items-center justify-center gap-8 bg-white/5 rounded-mag border border-white/10 backdrop-blur-md">
      <p className="text-white/80 text-sm text-center max-w-md">
        Every AI response is checked along this chain. Click a step or use Next to see what each part means.
      </p>
      <div className="flex flex-wrap justify-center gap-3 md:gap-6 items-center">
        {TRACE_NODES.map((node, i) => {
          const Icon = node.icon;
          const isActive = i === step;
          return (
            <React.Fragment key={node.label}>
              <button
                type="button"
                onClick={() => setStep(i)}
                className={`flex flex-col items-center gap-2 transition-all duration-300 rounded-2xl p-4 min-w-[72px] ${
                  isActive ? 'bg-magazine-accent text-white shadow-lg scale-110' : 'bg-white/10 text-white/60 hover:bg-white/20 hover:text-white/80'
                }`}
                aria-pressed={isActive}
                aria-label={`Step ${i + 1}: ${node.short}`}
              >
                <Icon size={28} />
                <span className="font-mono text-xs font-bold tracking-widest">{node.label}</span>
              </button>
              {i < maxStep && (
                <ArrowRight className="hidden md:block w-5 h-5 text-white/30 flex-shrink-0" aria-hidden />
              )}
            </React.Fragment>
          );
        })}
      </div>
      <AnimatePresence mode="wait">
        <motion.div
          key={step}
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -8 }}
          className="text-center"
        >
          <p className="text-magazine-accent font-bold text-lg mb-1">{TRACE_NODES[step].label}</p>
          <p className="text-white/90 text-base">{TRACE_NODES[step].short}</p>
        </motion.div>
      </AnimatePresence>
      <div className="flex gap-4">
        <button
          type="button"
          onClick={() => setStep((s) => (s <= 0 ? maxStep : s - 1))}
          className="text-[10px] font-bold uppercase tracking-widest text-white/60 hover:text-white"
        >
          Previous
        </button>
        <button
          type="button"
          onClick={() => setStep((s) => (s >= maxStep ? 0 : s + 1))}
          className="text-[10px] font-bold uppercase tracking-widest text-white/60 hover:text-white"
        >
          Next
        </button>
      </div>
    </div>
  );
};

// ——— 3. Invariant Simulator (one example: "I'm done") ———
export const InvariantSimulator: React.FC = () => {
  const [showWith, setShowWith] = useState(false);

  return (
    <div className="w-full max-w-2xl mx-auto p-6 md:p-10 bg-white rounded-mag border border-magazine-text/10 shadow-sm">
      <p className="text-center text-magazine-silver text-sm mb-6 font-medium">
        Example: AI says &ldquo;I&rsquo;m done&rdquo; but there&rsquo;s no file or proof
      </p>
      <div className="flex gap-4 justify-center mb-6">
        <button
          type="button"
          onClick={() => setShowWith(false)}
          className={`pill-button py-2 px-6 text-sm font-bold uppercase tracking-wider transition-all ${
            !showWith ? 'bg-magazine-text text-white' : 'border border-magazine-text/20 hover:bg-magazine-bg'
          }`}
        >
          Without PROACTIVE
        </button>
        <button
          type="button"
          onClick={() => setShowWith(true)}
          className={`pill-button py-2 px-6 text-sm font-bold uppercase tracking-wider transition-all ${
            showWith ? 'bg-magazine-accent text-white' : 'border border-magazine-text/20 hover:bg-magazine-bg'
          }`}
        >
          With PROACTIVE
        </button>
      </div>
      <AnimatePresence mode="wait">
        {!showWith ? (
          <motion.div
            key="without"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="space-y-4 p-6 rounded-xl bg-red-50 border-2 border-red-200"
          >
            <p className="font-bold text-magazine-text">The AI&rsquo;s message goes straight to you.</p>
            <p className="text-sm text-magazine-silver">You might act on it. If nothing was actually done, you lose time or make wrong decisions.</p>
          </motion.div>
        ) : (
          <motion.div
            key="with"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="space-y-4 p-6 rounded-xl bg-green-50 border-2 border-green-200"
          >
            <p className="font-bold text-magazine-text">PROACTIVE checks: &ldquo;Show me the artifact.&rdquo;</p>
            <p className="text-sm text-magazine-silver">No artifact? The &ldquo;Done&rdquo; claim is blocked. You see the truth instead of a confident lie.</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

// ——— 4. Safety Tier Simulator (click tier for example) ———
const TIER_EXAMPLES = [
  { label: 'Blocked', color: 'bg-magazine-text', example: '"I deleted those files"', action: 'PROACTIVE blocks until there is proof.' },
  { label: 'Escalated', color: 'bg-magazine-silver', example: '"This code has no bugs"', action: 'Flagged: need evidence or say "I’m not sure."' },
  { label: 'Constrained', color: 'bg-magazine-accent/50', example: 'Factual claim with medium confidence', action: 'Allowed with clear uncertainty if needed.' },
  { label: 'Monitored', color: 'bg-magazine-accent/80', example: 'Low-stakes opinion', action: 'Logged; usually allowed.' },
  { label: 'Harmless', color: 'bg-magazine-accent', example: '"I don’t know" or well-supported answer', action: 'Allowed.' },
];

export const SafetyTierSimulator: React.FC = () => {
  const [selected, setSelected] = useState<number | null>(null);

  return (
    <div className="w-full p-6 bg-white rounded-mag border border-magazine-text/10 shadow-sm">
      <p className="text-center text-magazine-silver text-sm mb-6 font-medium">
        Click a bar to see what PROACTIVE does at that risk level
      </p>
      <div className="flex gap-3 items-end h-40">
        {TIER_EXAMPLES.map((tier, i) => (
          <button
            key={i}
            type="button"
            onClick={() => setSelected(selected === i ? null : i)}
            className={`flex-1 flex flex-col items-center gap-2 transition-all rounded-t-xl min-h-[24px] ${
              tier.color
            } ${selected === i ? 'ring-4 ring-magazine-accent ring-offset-2 scale-105' : 'hover:opacity-90'}`}
            style={{ height: `${(i + 1) * 20}%`, minHeight: 48 }}
            aria-pressed={selected === i}
            aria-label={`${tier.label}: ${tier.example}`}
          >
            <span className="text-[8px] md:text-[9px] font-bold uppercase text-white opacity-90 mt-2">
              {tier.label}
            </span>
          </button>
        ))}
      </div>
      <AnimatePresence>
        {selected !== null && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="mt-6 p-4 rounded-xl bg-magazine-bg border border-magazine-text/10 overflow-hidden"
          >
            <p className="font-mono text-xs text-magazine-accent font-bold uppercase tracking-wider mb-2">
              {TIER_EXAMPLES[selected].label}
            </p>
            <p className="text-sm text-magazine-text font-medium">&ldquo;{TIER_EXAMPLES[selected].example}&rdquo;</p>
            <p className="text-sm text-magazine-silver mt-1">{TIER_EXAMPLES[selected].action}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

// ——— 5. PROACTIVE Letters: click/hover for plain-language definition ———
const PROACTIVE_LETTERS = [
  { letter: 'P', title: 'Privacy-First', plain: 'Use as little of your data as possible; keep it local by default.' },
  { letter: 'R', title: 'Reality-Bound', plain: 'Separate what we know from what we guess. Never pretend a guess is a fact.' },
  { letter: 'O', title: 'Observability', plain: 'Keep logs and reports so we can check what happened.' },
  { letter: 'A', title: 'Accessibility', plain: 'Keep things simple and clear for everyone.' },
  { letter: 'C', title: 'Constitutional', plain: 'Rules are rules. The AI can’t skip them to be "helpful."' },
  { letter: 'T', title: 'Truth or Bounded Unknown', plain: 'Say "I don’t know" when we don’t know. Don’t make things up.' },
  { letter: 'I', title: 'Intent Integrity', plain: 'Do exactly what you asked. If it’s unclear, ask before acting.' },
  { letter: 'V', title: 'Verification Before Action', plain: 'Check that something worked before saying it’s done.' },
  { letter: 'E', title: 'Error Ownership', plain: 'When something goes wrong, say so and fix it — don’t hide it.' },
];

export const ProactiveLettersSimulator: React.FC = () => {
  const [active, setActive] = useState<number | null>(null);

  return (
    <div className="flex flex-wrap justify-center gap-4 md:gap-6">
      {PROACTIVE_LETTERS.map((item, i) => (
        <button
          key={item.letter}
          type="button"
          onClick={() => setActive(active === i ? null : i)}
          onFocus={() => setActive(i)}
          onBlur={() => setActive(null)}
          className={`flex flex-col items-center p-4 rounded-xl border-2 transition-all min-w-[100px] ${
            active === i ? 'border-white bg-white/10 scale-105' : 'border-white/20 hover:border-white/40 hover:bg-white/5'
          }`}
          aria-expanded={active === i}
          aria-label={`${item.letter}: ${item.title}`}
        >
          <span className="font-mono text-2xl font-black text-white/80 mb-1">{item.letter}</span>
          <span className="text-xs font-bold text-white uppercase tracking-wider text-center">{item.title}</span>
          {active === i && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="mt-3 text-[10px] text-white/80 text-center leading-snug"
            >
              {item.plain}
            </motion.p>
          )}
        </button>
      ))}
    </div>
  );
};
