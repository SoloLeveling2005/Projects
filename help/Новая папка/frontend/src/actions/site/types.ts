import { ISite } from "../../types"

export enum SiteActionTypes {
    GET_SITES_SUCCESS = 'GET_SITES_SUCCESS',
    GET_SITES_FAIL = 'GET_SITES_FAIL'
} 


export interface GetSitesSuccess {
    type: SiteActionTypes.GET_SITES_SUCCESS
    payload: ISite[]
}

export interface GetSitesFail {
    type: SiteActionTypes.GET_SITES_FAIL
    payload?: unknown
}

type SiteType = GetSitesSuccess | GetSitesFail;

export default SiteType;
