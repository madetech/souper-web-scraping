import axios from "axios";

export default async function getReportList() {
    // let url = '/reports'
    // if(limit){
    //     url + `?limit=${limit}`
    // }
    // if(offset){
    //     url + `&offset=${offset}`
    // }
    const result = await axios.get('/reports')
        .then(res => res.status === 200 ? res.data : res.status)
        .catch(err => err);
    return result;
}