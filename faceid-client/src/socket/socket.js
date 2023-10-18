import { io } from "socket.io-client"

const api = import.meta.env.VITE_API

const sio = io(api)

export default sio
