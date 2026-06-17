import os

def clean_mac():
    print("Mac Optimization Started...")
    
    # User Caches
    os.system("rm -rf ~/Library/Caches/*")
    
    # System Logs
    os.system("rm -rf ~/Library/Logs/*")
    
    # Trash
    os.system("rm -rf ~/.Trash/*")
    
    # DNS Cache (Requires Admin Password)
    os.system("sudo dscacheutil -flushcache")
    os.system("sudo killall -HUP mDNSResponder")
    
    # Clear RAM (Requires Admin Password)
    os.system("sudo purge")
    
    print("Cleanup Completed!")

if __name__ == "__main__":
    clean_mac()