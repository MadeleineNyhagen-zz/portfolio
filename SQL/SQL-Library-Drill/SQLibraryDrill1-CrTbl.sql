USE dbLibrary
GO



CREATE TABLE Book (BookID INT NOT NULL PRIMARY KEY,
					Title VARCHAR(50) NULL,
					PublisherName VARCHAR(50) NULL,
					)
GO
CREATE TABLE Book_Authors (BookId INT NOT NULL,
					AuthorName VARCHAR(50) NULL)
GO
CREATE TABLE Publisher (Name VARCHAR(50) NOT NULL,
						[Address] VARCHAR(80) NULL,
						Phone VARCHAR(15) NULL)
GO
CREATE TABLE Library_Branch (BranchId INT NOT NULL PRIMARY KEY,
							BranchName VARCHAR(50) NULL,
							[Address] VARCHAR(80) NULL)
GO
CREATE TABLE Book_Copies (BookId INT NOT NULL,
						BranchId INT NOT NULL,
						No_Of_Copies INT NULL)
GO
CREATE TABLE Borrower (CardNo INT NOT NULL PRIMARY KEY,
						Name VARCHAR(50) NULL,
						[Address] VARCHAR(80) NULL,
						Phone VARCHAR(15) NULL)
GO
CREATE TABLE Book_Loans (BookId INT NOT NULL,
						BranchId INT NOT NULL,
						CardNo INT NOT NULL,
						DateOut DATE NULL,
						DueDate DATE NULL)
GO


