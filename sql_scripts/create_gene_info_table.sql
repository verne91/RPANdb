CREATE TABLE `gene_info` (
`gene_no` int(11) NOT NULL,
`source` char(10) DEFAULT NULL,
`chro` char(20) NOT NULL,
`start` int(11) NOT NULL,
`end` int(11) NOT NULL,
`strand` char(1) NOT NULL,
`cds_len` int(11) DEFAULT NULL,
`exon_num` int(11) DEFAULT NULL,
`gene_id` char(30) DEFAULT NULL,
PRIMARY KEY (`gene_no`),
KEY `gene_id` (`gene_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

