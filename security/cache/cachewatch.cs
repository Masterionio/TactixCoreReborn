using System;
using System.IO;

class CacheWatch
{
    static void Main()
    {
        var watcher = new FileSystemWatcher("./cache");
        watcher.IncludeSubdirectories = false;
        watcher.NotifyFilter = NotifyFilters.FileName | NotifyFilters.LastWrite;
        watcher.Changed += (s, e) => Console.WriteLine($"[WATCH] Changed: {e.FullPath}");
        watcher.Created += (s, e) => Console.WriteLine($"[WATCH] Created: {e.FullPath}");
        watcher.Deleted += (s, e) => Console.WriteLine($"[WATCH] Deleted: {e.FullPath}");
        watcher.Renamed += (s, e) => Console.WriteLine($"[WATCH] Renamed: {e.OldFullPath} → {e.FullPath}");

        watcher.EnableRaisingEvents = true;

        Console.WriteLine("[CACHEGUARD] Monitoring cache folder. Press Enter to stop.");
        Console.ReadLine();
    }
}
