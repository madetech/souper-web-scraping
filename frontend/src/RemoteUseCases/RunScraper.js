import axios from "axios";

export default async function runScrape(id) {
    const result = await axios.get(`http://localhost:8000/scrape`)
        .then(res => res.status)
        .catch(err => err);
    return result;
}