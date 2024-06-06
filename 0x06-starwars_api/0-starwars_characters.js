#!/usr/bin/node

const request = require("request");
const movieID = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error("Error:", error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error("Error:", error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
