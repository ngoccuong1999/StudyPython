using System;
using Tamir.IPLib;
namespace NapierCapture {
    public class ShowDevices {
        public static void Main(string[] args) {
            string verWinPCap = null;
            int count = 0;
            verWinPCap = Tamir
                .IPLib
                .Version
                .GetVersionString();
            PcapDeviceList getNetConnections = SharpPcap.GetAllDevices();
            Console.WriteLine("WinPCap Version: {0}", verWinPCap);
            Console.WriteLine("Connected devices:\r\n");
            foreach(PcapDevice net in getNetConnections) {
                Console.WriteLine("{0}) {1}", count, net.PcapDescription);
                Console.WriteLine("\tName:\t{0}", net.PcapName);
                Console.WriteLine("\tMode:\t\t\t{0}", net.PcapMode);
                Console.WriteLine("\tIP Address: \t\t{0}", net.PcapIpAddress);
                Console.WriteLine("\tLoopback: \t\t{0}", net.PcapLoopback);
                Console.WriteLine();
                count++;
            }
            Console.Write("Press any <RETURN> to exit");
            Console.Read();
        }
    }
}