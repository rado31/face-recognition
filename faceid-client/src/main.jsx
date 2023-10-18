import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import { ConfigProvider } from 'antd'
import { theme } from './ant-config/config.js'

ReactDOM.createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <ConfigProvider theme={theme}>
            <App />
        </ConfigProvider>
    </BrowserRouter>,
)
