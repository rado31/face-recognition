import { config } from 'dotenv'

config()

const env = {
    host: process.env.HOST,
    port: process.env.PORT,
}

export default env
