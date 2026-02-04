import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GoogleGenAI, Type } from "@google/genai";
import { Sparkles, X, Send, Loader2, Wand2, RefreshCw } from 'lucide-react';

interface ContentEditorProps {
  currentData: any;
  dataType: 'milestones' | 'genesis' | 'invariants';
  onUpdate: (newData: any) => void;
  isOpen: boolean;
  onClose: () => void;
}

export const ContentEditor: React.FC<ContentEditorProps> = ({ 
  currentData, 
  dataType, 
  onUpdate, 
  isOpen, 
  onClose 
}) => {
  const [prompt, setPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUpdate = async () => {
    if (!prompt.trim()) return;
    setIsLoading(true);
    setError(null);

    try {
      const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
      
      let schema: any;
      let systemInstruction = "";

      if (dataType === 'milestones') {
        systemInstruction = "You are a senior technical writer for a research journal. Update the milestones based on the user's request. Maintain the high-end, serious, and forensic tone of Intentional AI.";
        schema = {
          type: Type.ARRAY,
          items: {
            type: Type.OBJECT,
            properties: {
              year: { type: Type.STRING },
              title: { type: Type.STRING },
              description: { type: Type.STRING },
              extended: { type: Type.STRING }
            },
            required: ["year", "title", "description", "extended"]
          }
        };
      } else if (dataType === 'genesis') {
        systemInstruction = "Update the 'Genesis' chapter content. Provide a new title, subtitle, and body paragraph.";
        schema = {
          type: Type.OBJECT,
          properties: {
            title: { type: Type.STRING },
            quote: { type: Type.STRING },
            attribution: { type: Type.STRING },
            body: { type: Type.STRING }
          },
          required: ["title", "quote", "attribution", "body"]
        };
      } else if (dataType === 'invariants') {
        systemInstruction = "Update the 'Six Invariants'. Keep them as a list of exactly six items.";
        schema = {
          type: Type.ARRAY,
          items: {
            type: Type.OBJECT,
            properties: {
              id: { type: Type.STRING },
              title: { type: Type.STRING },
              desc: { type: Type.STRING }
            },
            required: ["id", "title", "desc"]
          }
        };
      }

      const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: `Current Content: ${JSON.stringify(currentData)}\n\nUser Request: ${prompt}`,
        config: {
          systemInstruction,
          responseMimeType: "application/json",
          responseSchema: schema,
        },
      });

      const updatedContent = JSON.parse(response.text);
      onUpdate(updatedContent);
      setPrompt('');
      onClose();
    } catch (err) {
      console.error(err);
      setError("Failed to process neural re-weighting. Please check connection.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div 
          initial={{ opacity: 0, y: 100 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 100 }}
          className="fixed bottom-8 left-1/2 -translate-x-1/2 w-full max-w-2xl z-50 px-4"
        >
          <div className="bg-magazine-text text-white rounded-3xl p-6 shadow-2xl border border-white/10 backdrop-blur-xl">
            <div className="flex justify-between items-center mb-6">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-magazine-accent flex items-center justify-center">
                  <Sparkles size={16} className="text-white" />
                </div>
                <div>
                  <h3 className="font-serif text-lg leading-none">Neural Content Editor</h3>
                  <p className="text-[9px] font-mono uppercase tracking-widest text-white/40 mt-1">
                    Modifying: {dataType.toUpperCase()} DATA_STREAM
                  </p>
                </div>
              </div>
              <button onClick={onClose} className="hover:rotate-90 transition-transform p-1">
                <X size={20} className="text-white/40 hover:text-white" />
              </button>
            </div>

            <div className="relative mb-4">
              <textarea
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="e.g., 'Make the milestones more aggressive and focused on cybersecurity forensics' or 'Rewrite the Genesis section for a lay audience'..."
                className="w-full bg-white/5 border border-white/10 rounded-xl p-4 text-sm placeholder:text-white/20 focus:outline-none focus:ring-1 focus:ring-magazine-accent min-h-[120px] resize-none"
              />
              {error && (
                <div className="absolute bottom-4 left-4 text-[10px] text-magazine-accent font-bold uppercase tracking-wider">
                  {error}
                </div>
              )}
            </div>

            <div className="flex justify-between items-center">
              <div className="flex gap-4">
                <button 
                  onClick={() => setPrompt("Make this more academic and formal.")}
                  className="text-[9px] font-bold uppercase tracking-widest text-white/40 hover:text-magazine-accent transition-colors"
                >
                  Formal
                </button>
                <button 
                  onClick={() => setPrompt("Explain this like I'm a systems engineer.")}
                  className="text-[9px] font-bold uppercase tracking-widest text-white/40 hover:text-magazine-accent transition-colors"
                >
                  Technical
                </button>
              </div>
              <button
                disabled={isLoading || !prompt.trim()}
                onClick={handleUpdate}
                className={`pill-button py-2 px-8 flex items-center gap-2 text-sm font-bold uppercase tracking-widest transition-all ${
                  isLoading ? 'bg-white/10 text-white/40' : 'bg-magazine-accent text-white hover:brightness-110'
                }`}
              >
                {isLoading ? (
                  <>
                    <Loader2 size={16} className="animate-spin" />
                    Re-weighting...
                  </>
                ) : (
                  <>
                    <RefreshCw size={16} />
                    Apply Changes
                  </>
                )}
              </button>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};
