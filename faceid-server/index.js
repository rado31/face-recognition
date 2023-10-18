import express from 'express'
import env from './config/config.js'
import cors from 'cors'
import students from './data/data.js'
import { Server } from 'socket.io'
import { createServer } from 'http'

const app = express()
const server = createServer(app)
const sio = new Server(server, {
    cors: {
        origin: '*',
    },
})

app.use(cors())
app.use(express.json())
app.use(express.static('data'))

app.get('/ping', (_, res) => res.send('pong'))

app.get('/user/:id', (req, res) => {
    const id = req.params.id
    const student = students[id] ? students[id] : undefined

    if (student) sio.emit('student', student)

    res.send()
})

sio.on('connect', socket => {
    console.log(socket.id)
    socket.on('disconnect', reason => console.log(reason, socket.id))
})

server.listen(env.port, env.host, () =>
    console.log(`http://${env.host}:${env.port}`),
)
