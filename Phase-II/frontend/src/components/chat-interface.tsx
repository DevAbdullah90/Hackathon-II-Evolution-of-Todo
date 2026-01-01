'use client';

import { useAgentChat } from '@/hooks/use-agent-chat';
import { useRef, useEffect, useState } from 'react';
import { Send, Bot, User, Sparkles, Wrench } from 'lucide-react';

export function ChatInterface() {
    const { messages, append, isLoading, userId } = useAgentChat();
    const [localInput, setLocalInput] = useState('');
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSend = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!localInput.trim()) return;

        const content = localInput;
        setLocalInput('');

        try {
            await append({
                role: 'user',
                content: content
            });
        } catch (err) {
            console.error("Error in append:", err);
        }
    };

    if (!userId) {
        return (
            <div className="h-full flex items-center justify-center p-4 text-[var(--text-secondary)] bg-[var(--card-bg)] rounded-3xl border border-white/5">
                <p>Please log in to access Taskoo Chat.</p>
            </div>
        );
    }

    return (
        <div className="flex flex-col h-[600px] w-full bg-[var(--card-bg)] rounded-3xl shadow-xl border border-white/5 overflow-hidden font-sans">
            {/* Header */}
            <div className="px-6 py-4 border-b border-white/5 bg-white/5 backdrop-blur-md flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-[var(--primary-gradient-from)] to-[var(--primary-gradient-to)] flex items-center justify-center shadow-lg">
                    <Bot size={18} className="text-white" />
                </div>
                <div>
                    <h2 className="font-semibold text-white tracking-wide">Taskoo AI</h2>
                    <p className="text-xs text-[var(--text-secondary)] flex items-center gap-1">
                        <span className="w-2 h-2 rounded-full bg-[var(--accent-green)] animate-pulse"></span>
                        Online
                    </p>
                </div>
            </div>

            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6 scrollbar-thin scrollbar-thumb-gray-700 scrollbar-track-transparent">
                {messages.length === 0 && (
                    <div className="h-full flex flex-col items-center justify-center text-center opacity-50 space-y-4 mt-10">
                        <div className="w-16 h-16 rounded-2xl bg-[var(--background)] flex items-center justify-center mb-4">
                            <Sparkles className="text-[var(--accent-yellow)]" size={32} />
                        </div>
                        <h3 className="text-xl font-bold text-white">How can I help you today?</h3>
                        <p className="text-[var(--text-secondary)] max-w-xs text-sm leading-relaxed">
                            Try asking me to add tasks, list your pending items, or organize your schedule.
                        </p>
                        <div className="grid grid-cols-2 gap-2 mt-6 w-full max-w-md">
                            {['Add a task to buy groceries', 'Show my pending tasks', 'Mark task #1 as done'].map((suggestion, i) => (
                                <button 
                                    key={i}
                                    onClick={() => setLocalInput(suggestion)}
                                    className="text-xs text-[var(--text-secondary)] bg-[var(--background)] p-3 rounded-xl hover:bg-white/5 transition-colors text-left border border-white/5"
                                >
                                    "{suggestion}"
                                </button>
                            ))}
                        </div>
                    </div>
                )}

                {messages.map((m) => (
                    <div key={m.id} className={`flex w-full ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`flex max-w-[85%] md:max-w-[75%] gap-3 ${m.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                            
                            {/* Avatar */}
                            <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center mt-1 shadow-md ${
                                m.role === 'user' 
                                    ? 'bg-[var(--accent-blue)]' 
                                    : 'bg-[var(--primary-gradient-from)]'
                            }`}>
                                {m.role === 'user' ? <User size={14} className="text-white" /> : <Sparkles size={14} className="text-white" />}
                            </div>

                            {/* Bubble */}
                            <div className={`flex flex-col gap-1 ${m.role === 'user' ? 'items-end' : 'items-start'}`}>
                                <div className={`px-5 py-3.5 rounded-2xl text-sm leading-relaxed shadow-sm backdrop-blur-sm ${
                                    m.role === 'user'
                                        ? 'bg-[var(--accent-blue)] text-white rounded-tr-sm'
                                        : 'bg-[var(--background)] text-[var(--text-primary)] border border-white/5 rounded-tl-sm'
                                }`}>
                                    <div className="whitespace-pre-wrap">{m.content}</div>
                                </div>

                                {/* Tool Invocations */}
                                {m.toolInvocations?.map((tool) => (
                                    <div key={tool.toolCallId} className="flex items-center gap-2 text-xs text-[var(--text-secondary)] bg-black/20 px-3 py-1.5 rounded-full border border-white/5 mt-1">
                                        <Wrench size={12} className="opacity-70" />
                                        <span className="font-mono opacity-80">Used tool: {tool.toolName}</span>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                ))}

                {isLoading && (
                    <div className="flex justify-start w-full">
                        <div className="flex items-center gap-3">
                            <div className="w-8 h-8 rounded-full bg-[var(--primary-gradient-from)] flex items-center justify-center">
                                <Bot size={14} className="text-white" />
                            </div>
                            <div className="bg-[var(--background)] px-4 py-3 rounded-2xl rounded-tl-sm border border-white/5 flex gap-1 items-center">
                                <span className="w-1.5 h-1.5 bg-[var(--text-secondary)] rounded-full animate-bounce [animation-delay:-0.3s]"></span>
                                <span className="w-1.5 h-1.5 bg-[var(--text-secondary)] rounded-full animate-bounce [animation-delay:-0.15s]"></span>
                                <span className="w-1.5 h-1.5 bg-[var(--text-secondary)] rounded-full animate-bounce"></span>
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="p-4 bg-[var(--card-bg)] border-t border-white/5">
                <form onSubmit={handleSend} className="relative flex items-center group">
                    <input
                        className="w-full bg-[var(--background)] text-white placeholder-gray-500 rounded-full py-3.5 pl-6 pr-12 focus:outline-none focus:ring-2 focus:ring-[var(--accent-blue)]/50 transition-all border border-white/5 shadow-inner"
                        value={localInput}
                        onChange={(e) => setLocalInput(e.target.value)}
                        placeholder="Type a message..."
                        disabled={isLoading}
                    />
                    <button
                        type="submit"
                        disabled={isLoading || !localInput.trim()}
                        className="absolute right-2 p-2 bg-[var(--accent-blue)] text-white rounded-full hover:bg-[var(--accent-blue)]/80 transition-colors disabled:opacity-50 disabled:bg-transparent disabled:text-gray-600"
                    >
                        <Send size={18} className={isLoading || !localInput.trim() ? "" : "ml-0.5"} />
                    </button>
                </form>
                <div className="text-center mt-2">
                    <p className="text-[10px] text-[var(--text-secondary)] opacity-50">
                        Taskoo can make mistakes. Please verify important info.
                    </p>
                </div>
            </div>
        </div>
    );
}