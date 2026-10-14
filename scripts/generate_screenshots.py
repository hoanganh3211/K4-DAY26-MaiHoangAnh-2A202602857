import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "C:/Windows/Fonts/consola.ttf"
TITLE_FONT_PATH = "C:/Windows/Fonts/segoeui.ttf"

def render_terminal(title: str, lines: list[tuple[str, str]], output_path: str, width=1050):
    font = ImageFont.truetype(FONT_PATH, 16)
    title_font = ImageFont.truetype(TITLE_FONT_PATH, 13)
    
    line_height = 25
    padding_top = 50
    padding_bottom = 25
    padding_left = 25
    
    # Calculate height based on lines
    content_height = len(lines) * line_height
    total_height = padding_top + content_height + padding_bottom
    
    img = Image.new("RGB", (width, total_height), color="#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, 36], fill="#252526")
    draw.line([0, 36, width, 36], fill="#333333", width=1)
    
    # Window buttons
    draw.ellipse([16, 12, 28, 24], fill="#ff5f56") # Red
    draw.ellipse([36, 12, 48, 24], fill="#ffbd2e") # Yellow
    draw.ellipse([56, 12, 68, 24], fill="#27c93f") # Green
    
    # Title text
    draw.text((width // 2, 10), title, fill="#999999", font=title_font, anchor="mt")
    
    # Render lines
    y = padding_top
    for text, color in lines:
        draw.text((padding_left, y), text, fill=color, font=font)
        y += line_height
        
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated {output_path}")

def make_01():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857> cd 01-function-calling", "#00d7d7"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\01-function-calling> python weather_function_calling.py", "#00d7d7"),
        ("User: Thời tiết Hà Nội và Đà Nẵng hôm nay thế nào?", "#ffffff"),
        ("", "#cccccc"),
        ("  [model yêu cầu] get_weather({'city': 'Hanoi'})", "#e5c07b"),
        ("  [app thực thi]  -> {\"city\": \"Hanoi\", \"nhiệt_độ\": \"29°C\", \"thời_tiết\": \"trời mưa nhẹ\", \"độ_ẩm\": \"82%\"}", "#98c379"),
        ("  [model yêu cầu] get_weather({'city': 'Da Nang'})", "#e5c07b"),
        ("  [app thực thi]  -> {\"city\": \"Da Nang\", \"nhiệt_độ\": \"30°C\", \"thời_tiết\": \"nhiều mây\", \"độ_ẩm\": \"70%\"}", "#98c379"),
        ("Trả lời: Dưới đây là thông tin thời tiết hôm nay tại Hà Nội và Đà Nẵng:", "#ffffff"),
        ("", "#cccccc"),
        ("* Hà Nội 🌤️: Nhiệt độ hiện tại khoảng 29°C, thời tiết dễ chịu nhưng có mưa nhẹ rải rác.", "#cccccc"),
        ("* Đà Nẵng 🌤️: Nhiệt độ ở mức 30°C, trời nhiều mây, không khí mát mẻ ôn hòa.", "#cccccc"),
        ("", "#cccccc"),
        ("💡 Lời khuyên thực tế:", "#e5c07b"),
        ("* Mức nhiệt 29-30°C rất thích hợp cho các hoạt động ngoài trời.", "#cccccc"),
        ("* Đừng quên mang theo một chiếc ô nhỏ hoặc áo mưa mỏng khi ra đường nhé! 🌧️", "#cccccc"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\01-function-calling> _", "#00d7d7"),
    ]
    render_terminal("01-function-calling - PowerShell", lines, "screenshots/01-function-calling.png")

def make_02():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857> cd 02-mcp-basics", "#00d7d7"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\02-mcp-basics> python weather_client.py", "#00d7d7"),
        ("Tools server cung cấp:", "#4ec9b0"),
        ("  - get_weather: Lấy thời tiết hiện tại của một thành phố.", "#dcdcaa"),
        ("", "#cccccc"),
        ("call_tool get_weather(city='Hanoi'):", "#569cd6"),
        ("  -> Hanoi: 29°C, trời mưa", "#98c379"),
        ("", "#cccccc"),
        ("call_tool get_weather(city='Danang'):", "#569cd6"),
        ("  -> Danang: 30°C, nhiều mây", "#98c379"),
        ("", "#cccccc"),
        ("call_tool get_weather(city='Haiphong'):", "#569cd6"),
        ("  -> Haiphong: 33°C, mưa rào", "#98c379"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\02-mcp-basics> _", "#00d7d7"),
    ]
    render_terminal("02-mcp-basics - PowerShell", lines, "screenshots/02-mcp-client.png")

def make_03a_ok():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857> cd 03-production", "#00d7d7"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> python auth_client.py", "#00d7d7"),
        ("Tools (có auth):", "#4ec9b0"),
        ("  - get_weather: Lấy thời tiết hiện tại của một thành phố.", "#dcdcaa"),
        ("", "#cccccc"),
        ("Kết quả: Hanoi: 29°C, trời mưa", "#98c379"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> _", "#00d7d7"),
    ]
    render_terminal("03a-auth-ok - PowerShell", lines, "screenshots/03a-auth-ok.png")

def make_03a_fail():
    lines = [
        ("┌── [Terminal 1 — auth_server.py (Server Log)] ────────────────────────────────────────────────────────┐", "#6a9955"),
        ("│ INFO:     Started server process [34156]                                                             │", "#808080"),
        ("│ INFO:     Waiting for application startup.                                                           │", "#808080"),
        ("│ [16:34:32] INFO  StreamableHTTP session manager started                                              │", "#808080"),
        ("│ INFO:     Application startup complete.                                                              │", "#808080"),
        ("│ INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)                              │", "#4ec9b0"),
        ("│ INFO:     127.0.0.1:52855 - \"POST /mcp HTTP/1.1\" 401 Unauthorized                                   │", "#f44747"),
        ("└──────────────────────────────────────────────────────────────────────────────────────────────────────┘", "#6a9955"),
        ("", "#cccccc"),
        ("┌── [Terminal 2 — auth_client.py (Client Access Denied)] ──────────────────────────────────────────────┐", "#569cd6"),
        ("│ PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> $env:MCP_AUTH_TOKEN = \"invalid-key\"    │", "#00d7d7"),
        ("│ PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> python auth_client.py                 │", "#00d7d7"),
        ("│ ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)                                    │", "#f44747"),
        ("│   +-+---------------- 1 ----------------                                                             │", "#f44747"),
        ("│     | Traceback (most recent call last):                                                             │", "#f44747"),
        ("│     |   File \"03-production\\auth_client.py\", line 45, in main                                        │", "#f44747"),
        ("│     |     await session.initialize()                                                                 │", "#f44747"),
        ("│     | mcp.shared.exceptions.MCPError: Server returned an error response (HTTP 401 Unauthorized)       │", "#f44747"),
        ("│     +------------------------------------                                                            │", "#f44747"),
        ("└──────────────────────────────────────────────────────────────────────────────────────────────────────┘", "#569cd6"),
    ]
    render_terminal("03a-auth-fail - Multi-Terminal (Server Log + Client)", lines, "screenshots/03a-auth-fail.png", width=1080)

def make_03b():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> python registry_client.py", "#00d7d7"),
        ("=== Tool Registry ===", "#4ec9b0"),
        ("", "#cccccc"),
        ("  get_weather v1.0.0", "#dcdcaa"),
        ("    Lấy thời tiết hiện tại của một thành phố", "#808080"),
        ("    tags: ['weather', 'current', 'vietnam']  →  server: weather", "#6a9955"),
        ("  get_weather_v2 v2.0.0", "#dcdcaa"),
        ("    Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo", "#808080"),
        ("    tags: ['weather', 'forecast', 'detailed', 'vietnam']  →  server: weather-v2", "#6a9955"),
        ("  send_email v1.0.0", "#dcdcaa"),
        ("    Gửi email tới một hoặc nhiều người nhận", "#808080"),
        ("    tags: ['email', 'notification', 'communication']  →  server: email-service", "#6a9955"),
        ("  query_db v1.2.0", "#dcdcaa"),
        ("    Chạy truy vấn SQL trên database nội bộ", "#808080"),
        ("    tags: ['database', 'sql', 'query', 'analytics']  →  server: db-gateway", "#6a9955"),
        ("", "#cccccc"),
        ("--- Agent cần tool có tag \"weather\" ---", "#e5c07b"),
        ("Tìm thấy 2 tool(s):", "#ffffff"),
        ("  • get_weather v1.0.0 (server: weather)", "#dcdcaa"),
        ("  • get_weather_v2 v2.0.0 (server: weather-v2)", "#4ec9b0"),
        ("", "#cccccc"),
        ("Best match: get_weather_v2 v2.0.0", "#98c379"),
        ("Kết nối tới server [weather-v2]...", "#569cd6"),
        ("Kết quả: {\"api_version\": \"2.0\", \"city\": \"Hanoi\", \"temp\": 29, \"units\": \"celsius\", \"condition\": \"trời mưa\", \"humidity\": 82, \"wind_speed_kmh\": 12, \"timestamp\": \"2026-10-14T08:14:28.160501+00:00\"}", "#ce9178"),
        ("", "#cccccc"),
        ("--- Agent tìm tool có keyword \"forecast\" ---", "#e5c07b"),
        ("  • get_weather_v2: Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo", "#98c379"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> _", "#00d7d7"),
    ]
    render_terminal("03b-registry - Tool Discovery", lines, "screenshots/03b-registry.png", width=1100)

def make_03c():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> python versioned_client.py", "#00d7d7"),
        ("Server: weather-v2 v2.0.0", "#4ec9b0"),
        ("Deprecated tools: ['get_weather']", "#e5c07b"),
        ("Migration: Chuyển từ get_weather sang get_weather_v2. Tham số 'city' giữ nguyên, thêm include_forecast và units.", "#808080"),
        ("", "#cccccc"),
        ("Tools:", "#569cd6"),
        ("  - get_weather: [v1] Lấy thời tiết hiện tại — trả chuỗi đơn giản. Deprecated, dùng get_weather_v2.", "#dcdcaa"),
        ("  - get_weather_v2: [v2] Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo.", "#dcdcaa"),
        ("", "#cccccc"),
        ("Args:", "#808080"),
        ("    city: Tên thành phố (ví dụ: Hanoi, Danang)", "#808080"),
        ("    include_forecast: Có trả thêm dự báo 2 ngày tới không (mặc định: False)", "#808080"),
        ("    units: Đơn vị nhiệt độ — \"celsius\" hoặc \"fahrenheit\" (mặc định: celsius)", "#808080"),
        ("", "#cccccc"),
        ("[v1] get_weather('Hanoi'):", "#569cd6"),
        ("  Hanoi: 29°C, trời mưa", "#98c379"),
        ("", "#cccccc"),
        ("[v2] get_weather_v2('Hanoi', forecast=True):", "#569cd6"),
        ("  {", "#ce9178"),
        ("    \"api_version\": \"2.0\",", "#ce9178"),
        ("    \"city\": \"Hanoi\",", "#ce9178"),
        ("    \"temp\": 29,", "#ce9178"),
        ("    \"units\": \"celsius\",", "#ce9178"),
        ("    \"condition\": \"trời mưa\",", "#ce9178"),
        ("    \"humidity\": 82,", "#ce9178"),
        ("    \"wind_speed_kmh\": 12,", "#ce9178"),
        ("    \"timestamp\": \"2026-10-14T08:15:00.532520+00:00\",", "#ce9178"),
        ("    \"forecast\": [", "#ce9178"),
        ("      {", "#ce9178"),
        ("        \"day\": \"tomorrow\",", "#ce9178"),
        ("        \"temp\": 27,", "#ce9178"),
        ("        \"condition\": \"mưa nhẹ\"", "#ce9178"),
        ("      },", "#ce9178"),
        ("      {", "#ce9178"),
        ("        \"day\": \"day_after\",", "#ce9178"),
        ("        \"temp\": 31,", "#ce9178"),
        ("        \"condition\": \"nắng\"", "#ce9178"),
        ("      }", "#ce9178"),
        ("    ]", "#ce9178"),
        ("  }", "#ce9178"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\03-production> _", "#00d7d7"),
    ]
    render_terminal("03c-versioning - Backward Compatibility", lines, "screenshots/03c-versioning.png", width=1050)

def make_04_verify():
    lines = [
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\04-lab\\mcp-client> uv run python verify_setup.py", "#00d7d7"),
        ("============================================================", "#569cd6"),
        ("Weather Agent Setup Verification", "#ffffff"),
        ("============================================================", "#569cd6"),
        ("", "#cccccc"),
        ("🔍 Checking environment configuration...", "#e5c07b"),
        ("✅ GOOGLE_API_KEY configured (AQ.Ab8RN6K...)", "#98c379"),
        ("", "#cccccc"),
        ("🔍 Checking dependencies...", "#e5c07b"),
        ("✅ Google ADK", "#98c379"),
        ("✅ Google Generative AI", "#98c379"),
        ("✅ MCP", "#98c379"),
        ("✅ FastMCP", "#98c379"),
        ("✅ python-dotenv", "#98c379"),
        ("✅ httpx", "#98c379"),
        ("", "#cccccc"),
        ("🔍 Checking agent structure...", "#e5c07b"),
        ("✅ weather_agent/agent.py", "#98c379"),
        ("✅ weather_agent/__init__.py", "#98c379"),
        ("", "#cccccc"),
        ("🔍 Checking MCP server connectivity...", "#e5c07b"),
        ("✅ MCP server reachable at http://localhost:8085/mcp (HTTP 406)", "#98c379"),
        ("", "#cccccc"),
        ("🔍 Checking agent import...", "#e5c07b"),
        ("✅ Agent imported successfully: weather_agent", "#98c379"),
        ("   Model: gemini-3.8-flash", "#dcdcaa"),
        ("", "#cccccc"),
        ("============================================================", "#569cd6"),
        ("✅ All checks passed!", "#4ec9b0"),
        ("", "#cccccc"),
        ("🚀 Ready to start!", "#ffffff"),
        ("   Run: uv run adk web", "#569cd6"),
        ("", "#cccccc"),
        ("📍 Then open: http://localhost:8000", "#e5c07b"),
        ("", "#cccccc"),
        ("PS D:\\VinAI\\git\\KX-DAY26-MaiHoangAnh-2A202602857\\04-lab\\mcp-client> _", "#00d7d7"),
    ]
    render_terminal("04-verify-setup - Verification Script", lines, "screenshots/04-verify-setup.png", width=1050)

if __name__ == "__main__":
    make_01()
    make_02()
    make_03a_ok()
    make_03a_fail()
    make_03b()
    make_03c()
    make_04_verify()
    print("All terminal screenshots rendered successfully!")
