# 🏓 Local Network Ping Pong Game

✌ **Hi!**  
This project is a simple but fun **Ping Pong multiplayer game** designed to run over a **local network** using a **hotspot** or **ad-hoc network**.  
One device acts as the **server**, and the others connect as **clients**. Just update the IP address in the code to match the server, and you're ready to play!

---

## 🌐 How It Works

- The game is built using a client-server architecture.
- Devices must be connected to the same local network (Wi-Fi hotspot or ad-hoc).
- One device (usually a computer) runs the server code.
- Other devices connect using the server’s IP address.

---

## ✅ Features

- Simple multiplayer Ping Pong game over LAN
- Hotspot or ad-hoc network supported
- Easy IP configuration for server and clients
- Lightweight and fast

---

## ⚙️ Setup Instructions

### 1. Connect All Devices to Same Network

Use a phone’s hotspot or create an ad-hoc Wi-Fi network.

### 2. Run Server

On one device (preferably a PC), run:

```bash
python server.py
