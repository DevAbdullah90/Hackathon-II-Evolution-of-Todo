"use client"
import { useState, useEffect } from "react";
import DashboardHeader from "@/components/dashboard-header";
import CategoryGrid from "@/components/category-grid";
import OngoingTaskCard from "@/components/ongoing-task-card";
import TaskList from "@/components/task-list";
import Sidebar from "@/components/sidebar";
import { Plus } from "lucide-react";
import CreateTaskModal from "@/components/create-task-modal";
import { fetchWithAuth } from "@/lib/api";
import { authClient } from "@/lib/auth-client";
import { Task } from "@/lib/types";

export default function Home() {
  const [refreshKey, setRefreshKey] = useState(0);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [taskToEdit, setTaskToEdit] = useState<Task | null>(null);
  const [tasks, setTasks] = useState<Task[]>([]);
  const { data: session } = authClient.useSession();

  const refreshDashboard = () => {
    setRefreshKey(prev => prev + 1);
  };

  const handleTaskCreated = () => {
    refreshDashboard();
    setIsModalOpen(false);
    setTaskToEdit(null);
  };

  const handleEditTask = (task: Task) => {
    setTaskToEdit(task);
    setIsModalOpen(true);
  };

  useEffect(() => {
    if (!session?.user?.id) return;

    fetchWithAuth(`/${session.user.id}/tasks`)
      .then((data) => setTasks(data as Task[]))
      .catch(err => console.error(err));
  }, [session, refreshKey]);

  // Determine the "Ongoing" task (e.g., the most recent incomplete task)
  // Assuming API returns tasks in some order, or we just take the first incomplete one.
  const ongoingTask = tasks.find(t => !t.is_completed) || null;

  return (
    <div className="min-h-screen bg-[var(--background)] text-white font-sans selection:bg-[var(--accent-blue)] selection:text-white flex">

      {/* Desktop Sidebar */}
      <Sidebar />

      {/* Main Content Area */}
      <main className="flex-1 min-h-screen relative flex flex-col px-6 md:px-10 md:ml-64 w-full">

        {/* Header Section */}
        <div className="max-w-5xl w-full mx-auto">
          <DashboardHeader />
        </div>

        {/* Scrollable Content Area */}
        <div className="flex-1 flex flex-col gap-6 pb-24 max-w-5xl w-full mx-auto">

          {/* Top Row: Categories (expands on desktop) */}
          <CategoryGrid />

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Left Column: Ongoing Task & Stats */}
            <div className="col-span-1 lg:col-span-1 space-y-6">
              <OngoingTaskCard task={ongoingTask} />

              {/* Placeholder for small stats or calendar could go here to fill space */}
            </div>

            {/* Right Column: Task List (Takes more space on desktop) */}
            <div className="col-span-1 lg:col-span-2">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-lg font-bold">Todays Task</h2>
                <button className="text-[var(--primary-gradient-from)] text-sm">See all</button>
              </div>
              {/* Wrapped in a constrained height container for desktop scroll if needed, 
                    currently just letting it flow */}
              <TaskList
                tasks={tasks}
                onTaskUpdate={refreshDashboard}
                onEditTask={handleEditTask}
              />
            </div>
          </div>

        </div>

        {/* Floating Action Button */}
        <button
          onClick={() => {
            setTaskToEdit(null);
            setIsModalOpen(true);
          }}
          className="fixed bottom-8 right-8 w-16 h-16 bg-gradient-to-r from-[var(--primary-gradient-from)] to-[var(--primary-gradient-to)] rounded-full flex items-center justify-center shadow-lg shadow-orange-500/40 hover:scale-105 transition-transform z-50 md:right-12"
        >
          <Plus size={32} className="text-white" />
        </button>

        {/* Create Task Modal */}
        <CreateTaskModal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
          onTaskCreated={handleTaskCreated}
          taskToEdit={taskToEdit}
        />

      </main>
    </div>
  );
}
