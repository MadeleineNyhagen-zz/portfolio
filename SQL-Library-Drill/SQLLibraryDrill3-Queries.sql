--Query 1: How many copies of the book titled The Lost Tribe are owned by the library branch whose name is "Sharpstown"?
SELECT lb.BranchName, bc.No_Of_Copies, bk.Title
FROM Library_Branch AS lb
INNER JOIN Book_Copies AS bc
ON lb.BranchId = bc.BranchId
INNER JOIN Book AS bk
ON bc.BookId = bk.BookId
WHERE lb.BranchName = 'Sharpstown'
AND bc.BookId = 1

--Query 2: How many copies of the book titled The Lost Tribe are owned by each library branch?
SELECT lb.BranchName, bc.No_Of_Copies, bk.Title
FROM Library_Branch AS lb
INNER JOIN Book_Copies AS bc
ON lb.BranchId = bc.BranchId
INNER JOIN Book AS bk
ON bc.BookId = bk.BookId
WHERE bc.BookId = 1

--Query 3: Retrieve the names of all borrowers who do not have any books checked out.
SELECT br.Name, br.CardNo, bl.BookId
FROM Borrower AS br
LEFT OUTER JOIN Book_Loans AS bl
ON br.CardNo = bl.CardNo
WHERE bl.BookId IS NULL

--Query 4: For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today, retrieve the book title, the borrower's name, and the borrower's address.
SELECT bk.Title, br.Name, br.[Address]
FROM Library_Branch AS lb
INNER JOIN Book_Loans AS bl
ON lb.BranchId = bl.BranchId
INNER JOIN Borrower AS br
ON bl.CardNo = br.CardNo
INNER JOIN Book AS bk
ON bl.BookId = bk.BookID
WHERE lb.BranchId = 1
AND DueDate = '2015-10-01'

--Query 5: For each library branch, retrieve the branch name and the total number of books loaned out from that branch.
SELECT lb.BranchName, COUNT(bl.BookId) AS TotalBooksLoaned
FROM Library_Branch AS lb
LEFT OUTER JOIN Book_Loans AS bl
ON lb.BranchId = bl.BranchId
GROUP BY lb.BranchName

--Query 6: Retrieve the names, addresses, and number of books checked out for all borrowers who have more than five books checked out.
SELECT br.Name, br.[Address], brblcount.TotalBooksBorrowed
FROM
(SELECT br.CardNo, COUNT(bl.BookID) AS TotalBooksBorrowed
FROM Borrower AS br
INNER JOIN Book_Loans AS bl
ON br.CardNo = bl.CardNo
GROUP BY br.CardNo
) AS brblcount
INNER JOIN Borrower AS br
ON brblcount.CardNo = br.CardNo
WHERE brblcount.TotalBooksBorrowed > 5

--Query 7: For each book authored (or co-authored) by "Stephen King", retrieve the title and the number of copies owned by the library branch whose name is "Central"
SELECT bk.Title, ba.AuthorName, lb.BranchName, bc.No_Of_Copies
FROM Book AS bk
INNER JOIN Book_Authors AS ba
ON bk.BookID = ba.BookId
INNER JOIN Book_Copies AS bc
ON bk.BookID = bc.BookId
INNER JOIN Library_Branch AS lb
ON bc.BranchId = lb.BranchId
WHERE ba.AuthorName = 'Stephen King'
AND lb.BranchName = 'Central'
GO

--Stored procedure: To find how many copies each library has of a particular title

CREATE PROCEDURE NumberOfTitle @BookTitle NVARCHAR(30)
AS
SELECT lb.BranchName, bc.No_Of_Copies, bk.Title
FROM Library_Branch AS lb
INNER JOIN Book_Copies AS bc
ON lb.BranchId = bc.BranchId
INNER JOIN Book AS bk
ON bc.BookId = bk.BookId
WHERE bk.Title = @BookTitle
GO


EXEC NumberOfTitle @BookTitle = 'Misery'
GO
