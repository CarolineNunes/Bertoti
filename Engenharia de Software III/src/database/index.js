const Sequelize = require("sequelize");
require("dotenv").config();

let database = null;
try {
	console.log(process.env.BD_URL)
	database = new Sequelize('script','postgres','#Palmeiras123', {
		host: 'localhost',
		dialect: 'postgres' 
	});
	
	database
		.authenticate()
		.then(() => {
			console.log("Conexão realizada com o SGBD");
		})
		.catch((error) => {
			console.error("Não foi possível conectar com o SGBD:", error.message);
		});
} catch (e) {
	console.log(e.message);
}

module.exports = database;
