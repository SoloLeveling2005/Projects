import React from "react";
import './Main.css';
import logoImg from '../../assets/images/logo.png';
import {ReactComponent as SearchIcon} from '../../assets/icons/search.svg';
import userImg from '../../assets/images/user.png';
import { useTypedSelector } from "../../hooks/useRedux";
import Site from "../../components/Site/Site";
import { ISite } from "../../types";


const Main: React.FC = () => {

    const sites = useTypedSelector(state => state.sites.sites);

    return (
        <div className="home">
            <header className="home-header">
                <div className="container">
                    <div className="home-header__inner">
                        <div className="home-logo">
                            <img src={logoImg} alt="logo" className='home-logo__img'/>
                        </div>
                        <div className="home-search">   
                            <input 
                                className="home-search__input" 
                                type="text" 
                                placeholder="What you need?"
                            />
                            <div role={'button'} className="home-search__button">
                                <SearchIcon/>
                            </div>
                        </div>
                        <div className="home-auth">
                            <div className="home-auth__image">
                                <img src={userImg} alt="user" className="home-auth__img" />
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            <div className='home-main'>
                <div className="container">
                    <div className="home-main__inner">
                        <div className="home-main__sites">
                            {sites.map((site: ISite) => 
                            <Site 
                                title={site.title} 
                                ip={site.ip} 
                                description={site.description} 
                                key={site.id} 
                            />)}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Main;
