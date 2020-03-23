import sys
import psutil

# print("Arguments list: ", str(sys.argv), "\n") # Just for debug purpose

help_message = """\nTry 'python3 metrics.py --help' for more information
Or just use 'all' option to print all available server metrics."""

if len(sys.argv) == 1:
    print("metrics.py : Missing operand.", help_message)
    exit(2)

cpu_times = psutil.cpu_times()
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()

def cpu_metrics():  # Print CPU metrics
    # print("\nsystem.cpu.ALL: {}".format(cpu_times), "\n")  # Just for debug purpose
    # print("CPU metrics:\n")
    print("system.cpu.idle {}".format(cpu_times.idle))
    print("system.cpu.user {}".format(cpu_times.user))
    print("system.cpu.guest {}".format(cpu_times.guest))
    print("system.cpu.iowait {}".format(cpu_times.iowait))
    print("system.cpu.stolen {}".format(cpu_times.steal))
    print("system.cpu.system {}".format(cpu_times.system))

def mem_metrics():  # Print Memory metrics
    # Virtual
    # print("\nVirtual ALL: {}".format(virtual_memory), "\n")  # Just for debug purpose
    # print("Memory metrics:\n")
    print("virtual total {}".format(virtual_memory.total))
    print("virtual used {}".format(virtual_memory.used))
    print("virtual free {}".format(virtual_memory.free))
    print("virtual shared {}".format(virtual_memory.shared))
    # SWAP
    # print("\nSWAP ALL: {}".format(swap_memory), "\n")        # Just for debug purpose
    print("swap total {}".format(swap_memory.total))
    print("swap used {}".format(swap_memory.used))
    print("swap free {}".format(swap_memory.free))

def just4fun():
    liner = "-----------------------------------------------"
    print()
    print(liner)
    print("Welcome to the --> Metrics <-- Neo ;-)")
    print(liner, "\n")

def show_help():
    print("Usage: python3 metrics.py [OPTION]")
    print("Shows useful server metrics\n")
    print("Mandatory arguments to long options are mandatory for short options too.")
    print("  help, --help, -h                print this help info")
    print("  all, --all, -a                  show ALL available metrics")
    print("  cpu, --cpu, -c                  show CPU metrics")
    print("  mem, --mem, -m                  show Memory metrics")
    print("  ... to be continued")

# Todo: Rewrite if-else logic to implement a switch-case statement
if sys.argv[1] == 'all' or sys.argv[1] == '--all' or sys.argv[1] == '-a':
    cpu_metrics()
    mem_metrics()
else:
    if sys.argv[1] == 'cpu' or sys.argv[1] == '--cpu' or sys.argv[1] == '-c':
        cpu_metrics()
    else:
        if sys.argv[1] == 'mem' or sys.argv[1] == '--mem' or sys.argv[1] == '-m':
            mem_metrics()
        else:
            if sys.argv[1] == 'help' or sys.argv[1] == '--help' or sys.argv[1] == '-h':
                just4fun()
                show_help()
            else:
                print("metrics.py : Invalid option", str("'" + sys.argv[1] + "'"), help_message)
