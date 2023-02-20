import axios from "axios"



export const getSites = () => (dispatch: any) => {
    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }

    try {
        const res = axios.get('url', config)
    } catch(err) {

    }
}
