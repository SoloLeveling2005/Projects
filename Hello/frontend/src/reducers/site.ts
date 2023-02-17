interface ISite {
    id: number
    ip: string
    description: string
    title: string
}

interface IState {
    sites: ISite[]
}

const initialState: IState = {
    sites: []
}


const siteReducer = (state = initialState, action: any): IState => {
    const { type, payload } = action
    
    switch(type) {
        default:
            return state;
    }
}

export default siteReducer;
