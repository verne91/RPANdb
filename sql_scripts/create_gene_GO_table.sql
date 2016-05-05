CREATE TABLE `gene_go` (
`gene_no` int(11) NOT NULL,
`gene_id` char(30),
`go_id` char(15) ,
KEY `gene_no` (`gene_no`),
KEY `gene_id` (`gene_id`),
CONSTRAINT `go_seq_ibfk_1` FOREIGN KEY (`gene_no`) REFERENCES `gene_info` (`gene_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
