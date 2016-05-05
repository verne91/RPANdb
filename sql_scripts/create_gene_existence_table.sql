create table `gene_existence`(
`line_no` int not null,
`line_code` char(20) not null,
`gene_no` int not null,
`gene_id` char(30),
key `line_no` (`line_no`),
key `gene_no` (`gene_no`),
key `line_code` (`line_code`),
key `gene_id` (`gene_id`),
CONSTRAINT `gene_existence_ibfk_1` FOREIGN KEY (`line_no`) REFERENCES `line_info` (`line_no`),
CONSTRAINT `gene_existence_ibfk_2` FOREIGN KEY (`gene_no`) REFERENCES `gene_info` (`gene_no`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;