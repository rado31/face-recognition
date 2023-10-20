import { CloseOutlined } from '@ant-design/icons'
import { Card, Col, FloatButton, Image, Row } from 'antd'
import React from 'react'
import { io } from 'socket.io-client'

export default function List({ students, setStudents }) {
    return (
        <>
            {students.map((student, id) => (
                <Card key={id} style={{ marginTop: 50 }}>
                    <Row align={'middle'}>
                        <Col flex={'0 0 0'} style={{ marginRight: 25 }}>
                            <Image src={student.photo} width={100}></Image>
                        </Col>
                        <Col flex={'1 0 1'}>
                            <div>ID: {student.id}</div>
                            <div>Name: {student.name}</div>
                            <div>Surname: {student.surname}</div>
                            <div>DOB: {student.dob}</div>
                            <div>Faculty: {student.faculty}</div>
                            <div>Major: {student.major}</div>
                        </Col>
                    </Row>
                </Card>
            ))}

            <FloatButton
                icon={<CloseOutlined />}
                onClick={async () => {
                    localStorage.clear()
                    setStudents([])

                    await fetch('http://localhost:5000/clear')
                }}
            />
        </>
    )
}
