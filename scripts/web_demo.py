#!/usr/bin/env python3
"""简易Web演示服务器"""

import argparse
import http.server
import socketserver
import json

PORT = 8080

class SandboxHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                "version": "0.1.0",
                "status": "running",
                "available_datasets": ["current_response", "peek_fatigue", "extreme_scenarios"]
            }
            self.wfile.write(json.dumps(status).encode())
            return
        
        if self.path == '/':
            self.path = '/web/index.html'
        
        return super().do_GET()
    
    def log_message(self, format, *args):
        # 减少日志输出
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--data-dir', type=str, default='./data')
    args = parser.parse_args()
    
    with socketserver.TCPServer(("", args.port), SandboxHandler) as httpd:
        print(f"SINOSHOP-Sandbox 演示服务器运行在 http://localhost:{args.port}")
        print("按 Ctrl+C 停止")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")

if __name__ == "__main__":
    main()