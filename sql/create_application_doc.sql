create table application_docs (
	ApplicationDocsID int NOT NULL, 
    ApplicationDocsTypeID int NOT NULL,
    ApplNo char(6) NOT NULL,
    SubmissionType char(10) NOT NULL,
    SubmissionNo int NOT NULL,
    ApplicationDocsTitle varchar(100) null,
    ApplicationDocsURL varchar(255) null,
    ApplicationDocsDate datetime null
);

