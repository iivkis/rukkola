import express from "express"
import {handler} from "../build/handler"

let app = express();
app.use(handler);

app.listen(9091, ()=>{
    console.log("listen...")
})
