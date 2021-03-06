const router = require("express").Router();
const {TalhaoController} = require("../controllers");
const {create, remove, update, list} = new TalhaoController();

router.post("/create", create);
router.delete("/remove", remove);
router.put("/update", update);
router.get("/list", list);

router.use( (_, res) => {
	res.status(400).json({error:"Operação desconhecida com o talhão"});
});

module.exports = router;
