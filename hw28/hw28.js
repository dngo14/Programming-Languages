#!/usr/bin/node

let prettystring = ""
const parser = (string) => {
    if (string.includes("\n")) {
            lines = string.split("\n")
    }
        else {
            lines = string
        }
    let updatedline = string
        if (lines[0].slice(0,2) == "c ") {
            let words = lines[0].split(" ")
            //turtle.color(words[1], words[2])
            prettystring += "color\n"+words[1]+"\n"+words[2]+"\n"
            updatedline = updatedline.replace("c ", "");
            updatedline = updatedline.replace(words[1]+" ", "");
            updatedline = updatedline.replace(words[2]+"\n", "");
            parser(updatedline)
        }else if (lines[0].slice(0,7) == "fill { ") {
            //turtle.begin_fill()
            updatedline = updatedline.replace("fill { ", "")
            prettystring+="Fill Begin\n"
            parser(updatedline)
            prettystring+="Fill End\n"
        }else if(lines[0].slice(0,6) == "repeat") {
            updatedline = lines.slice(1, lines.length)
            let words = lines[0].split(" ")
            let reps = parseInt(words[1])
            prettystring+="Repeat "+words[1]+"\n"
            for (let i = 0; i < reps; i+=1) {
                parser(updatedline)
            }
            prettystring+="\n"
            //console.log(updatedline)
        } else if(lines[0].includes("f") || lines[0].includes("b") || lines[0].includes("l") || lines[0].includes("r") && lines[0].matches(".*\\d.*")) {
            let words = lines[0].split()
            for (let i = 0; i < words.length; i+=1) {
                prettystring+=words[i].replace("}}", "")+" "
            }
        }
    return updatedline
}

let x = "c green blue\nfill { repeat 36 {\nf200 l170}}"
let y = x.match(/{([^}]*)}/)[0]
//console.log(y.match(/[^{\}]+(?=})/g))
//console.log(x.split("\n"))
let z = parser("c green blue\nfill { repeat 36 {\nf200 l170}}")
//console.log(z)
console.log(prettystring)
