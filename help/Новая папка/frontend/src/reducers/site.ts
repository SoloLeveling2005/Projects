import { ISite } from "../types";
import SiteType, { SiteActionTypes } from "../actions/site/types";


interface IState {
    sites: ISite[]
}

const initialState: IState = {
    sites: []
}


const sites = (state = initialState, action: SiteType): IState => {
    const { type, payload } = action
    
    switch(type) {
        case SiteActionTypes.GET_SITES_SUCCESS:
            return {...state, sites: payload} 

        case SiteActionTypes.GET_SITES_FAIL:
            return state
        default:
            return state;
    }
}

export default sites;
