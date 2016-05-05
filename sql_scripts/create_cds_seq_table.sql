CREATE TABLE `cds_seq` (
`gene_no` int(11) NOT NULL,
`seq` text,
KEY `gene_no` (`gene_no`),
CONSTRAINT `cds_seq_ibfk_1` FOREIGN KEY (`gene_no`) REFERENCES `gene_info` (`gene_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
