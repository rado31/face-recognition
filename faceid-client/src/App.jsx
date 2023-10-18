import React, { useEffect, useState } from 'react'
import { Route, Routes } from 'react-router-dom'
import sio from './socket/socket'
import List from './components/List'
import Layout from './components/Layout'
import './index.css'

export default function App() {
    const [students, setStudents] = useState([])
    const [rerender, setRerender] = useState(false)

    useEffect(() => {
        sio.on('connect', () => console.log('connected to server'))

        sio.on('student', student => {
            localStorage.setItem(student.id, JSON.stringify(student))
            setRerender(!rerender)
        })

        return () => {
            sio.off('connect')
            sio.off('student')
        }
    }, [])

    useEffect(() => {
        // student ID
        const keys = Object.keys(localStorage)

        if (keys.length !== 0)
            keys.forEach(key => {
                const student = localStorage.getItem(key)
                setStudents(prev => [...prev, JSON.parse(student)])
            })
    }, [rerender])

    return (
        <Routes>
            <Route path='/' element={<Layout />}>
                <Route
                    path=''
                    element={<List students={students} setStudents={setStudents} />}
                />
            </Route>
        </Routes>
    )
}
