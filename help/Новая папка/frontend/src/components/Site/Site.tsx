import React from 'react';
import { Link } from 'react-router-dom';
import './Site.css';


interface SiteProps {
    title: string
    description: string
    ip: string
}

const Site: React.FC<SiteProps> = ({ip, description, title}) => {
    
    return (
        <div className='site'> 
            <div className='site-title'>
                <Link className='site-title__link' to={ip}>{title}</Link>
            </div>
            <div className='site-ip'>
                <Link className='site-ip__link' to={ip}>{ip}</Link>
            </div>
            <div className='site-description'>
                <p>{cutDescription(description)}</p>
            </div>
        </div>
    )
}

function cutDescription (description: string): string {
    if(description.length <= 300) 
        return description

    return `${description.slice(0, 300)}...` 
}

export default Site;
