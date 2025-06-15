using System;
using System.Diagnostics;

class MemGuard {
    static void Main() {
        Console.WriteLine("[C#] Top 5 memory-hungry processes:");
        var processes = Process.GetProcesses();
        Array.Sort(processes, (x, y) => y.WorkingSet64.CompareTo(x.WorkingSet64));

        for (int i = 0; i < 5 && i < processes.Length; i++) {
            Console.WriteLine($"{processes[i].ProcessName} – {processes[i].WorkingSet64 / 1024 / 1024} MB");
        }
    }
}
