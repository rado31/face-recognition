import { Row, Segmented } from 'antd'
import React from 'react'
import { Outlet, useNavigate } from 'react-router-dom'

export default function Layout() {
    const navigate = useNavigate()

    const options = [
        {
            label: 'List',
            value: '',
        },
    ]

    return (
        <>
            <Row justify={'center'}>
                <Segmented
                    size='large'
                    options={options}
                    onChange={url => navigate(url)}
                ></Segmented>
            </Row>
            <Row className='live_container' justify={'center'}>
                <Outlet />
            </Row>
        </>
    )
}
