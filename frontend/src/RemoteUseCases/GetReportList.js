import axios from "axios"

export default async function getList() {
    const result = await axios.get("http://localhost:8008/report", {
        headers: {'Access-Control-Allow-Origin': '*', "Content-Type": "application/json"}
    }).then(res =>  res.status === 200 ? res.data : res.status )
    .catch(err => err );
    
    return result;

}