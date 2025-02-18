import nmap

def scan_network(target="192.168.1.1"):
    """Faz uma varredura nas portas de um IP alvo."""
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-p 1-65535 -T4')

    results = {}
    for host in scanner.all_hosts():
        results[host] = scanner[host]['tcp']
    
    return results
