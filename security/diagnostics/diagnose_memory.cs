using System;
using System.Diagnostics;

class MemoryCheck
{
    static void Main()
    {
        Console.WriteLine("[SECURITY] Scanning for memory spikes...");
        Process[] processlist = Process.GetProcesses();

        foreach (Process p in processlist)
        {
            try
            {
                if (p.PrivateMemorySize64 > 500 * 1024 * 1024)  // >500MB
                {
                    Console.WriteLine($"[!] High memory process: {p.ProcessName} - {p.PrivateMemorySize64 / 1024 / 1024}MB");
                }
            }
            catch { }
        }
    }
}
