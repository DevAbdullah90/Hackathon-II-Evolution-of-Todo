import { LayoutGrid, Folder, Settings, LogOut, Calendar, MessageSquare } from "lucide-react";
import Image from "next/image";

export default function Sidebar() {
    const navItems = [
        { icon: LayoutGrid, label: "Overview", active: true },
        { icon: Calendar, label: "Calendar", active: false },
        { icon: Folder, label: "Projects", active: false },
        { icon: MessageSquare, label: "Messages", active: false },
        { icon: Settings, label: "Settings", active: false },
    ];

    return (
        <aside className="hidden md:flex w-64 flex-col h-screen fixed left-0 top-0 bg-[var(--card-bg)] border-r border-white/5 p-6 z-50">
            <div className="flex items-center gap-2 mb-10 px-2">
                <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-[var(--primary-gradient-from)] to-[var(--primary-gradient-to)] flex items-center justify-center font-bold text-white text-lg">
                    T
                </div>
                <span className="text-xl font-bold text-white tracking-tight">Taskoo</span>
            </div>

            <nav className="flex-1 flex flex-col gap-2">
                {navItems.map((item, idx) => (
                    <button
                        key={idx}
                        className={`flex items-center gap-3 px-4 py-3 rounded-2xl transition-all duration-200 group ${item.active
                                ? "bg-[var(--primary-gradient-from)] text-white shadow-lg shadow-orange-500/20"
                                : "text-[var(--text-secondary)] hover:bg-white/5 hover:text-white"
                            }`}
                    >
                        <item.icon size={20} />
                        <span className="font-medium text-sm">{item.label}</span>
                    </button>
                ))}
            </nav>

            <button className="flex items-center gap-3 px-4 py-3 text-[var(--text-secondary)] hover:text-white hover:bg-white/5 rounded-2xl transition-colors mt-auto">
                <LogOut size={20} />
                <span className="font-medium text-sm">Log Out</span>
            </button>
        </aside>
    );
}
