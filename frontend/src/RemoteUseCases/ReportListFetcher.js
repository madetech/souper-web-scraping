import axios from "axios";

export default async function getReportList() {
    const result = await axios.get(process.env.REACT_APP_HOST_IP_ADDRESS)
    .then(res => res.status === 200 ? res.data.items : res.status)
        .catch(err => err);

    return result;

}