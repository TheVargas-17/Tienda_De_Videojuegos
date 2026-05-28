-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla tienda_videojuegos.clientes: ~2 rows (aproximadamente)
INSERT INTO `clientes` (`id_cliente`, `nombre`, `telefono`, `correo`, `contrasena`) VALUES
	(1, 'leo', '6561098577', 'leo@gmail.com', '$2b$12$uKQTUO2QI1u2VqmKoAc5L.eA1F8Nl5G85yFS/Ptyjjh7Ft/0jHsYG'),
	(2, 'leo', '6561098577', 'leo1@gmail.com', '$2b$12$vUkOrknr9kB2ODETVFfniOkI/tkaW9ipjzHRqijmDeb3fmepE4QXu');

-- Volcando datos para la tabla tienda_videojuegos.consolas: ~3 rows (aproximadamente)
INSERT INTO `consolas` (`id_consola`, `nombre_consola`) VALUES
	(1, 'PlayStation 5'),
	(2, 'Xbox Series X'),
	(3, 'Nintendo Switch');

-- Volcando datos para la tabla tienda_videojuegos.juegos: ~6 rows (aproximadamente)
INSERT INTO `juegos` (`id_juego`, `nombre`, `precio`, `stock`, `id_consola`, `imagen`) VALUES
	(1, 'Spider-Man 2', 1499.99, 10, 1, 'spiderman.jpg'),
	(2, 'God of War Ragnarok', 1399.99, 8, 1, 'gow.jpg'),
	(3, 'Halo Infinite', 1299.99, 12, 2, 'halo.jpg'),
	(4, 'Forza Horizon 5', 1199.99, 7, 2, 'forza.jpg'),
	(5, 'The Legend of Zelda: Tears of the Kingdom', 1599.99, 15, 3, 'zelda.jpg'),
	(6, 'Mario Kart 8 Deluxe', 999.99, 20, 3, 'mariokart.jpg');

-- Volcando datos para la tabla tienda_videojuegos.ventas: ~2 rows (aproximadamente)
INSERT INTO `ventas` (`id_venta`, `id_cliente`, `id_juego`, `id_consola`, `fecha`) VALUES
	(4, 1, 5, 3, '2026-05-25'),
	(5, 1, 6, 3, '2026-05-25');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
