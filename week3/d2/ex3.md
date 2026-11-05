# API comparison

## GitHub: issue comments
List comments on one issue: GET /repos/{owner}/{repo}/issues/{issue_number}/comments
Create a comment on an issue: POST /repos/{owner}/{repo}/issues/{issue_number}/comments with body {"body": "Me too"}
Get one comment: GET /repos/{owner}/{repo}/issues/comments/{comment_id}
Update a comment: PATCH /repos/{owner}/{repo}/issues/comments/{comment_id} with body
Delete a comment: DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}

Does getting one comment use a nested or direct-style path?
direct style
Which of my review endpoints is most similar?
GET /reviews/7

## Stripe: customers
List customers: GET /v1/customers
Create a customer: POST /v1/customers with body
Get one customer: GET /v1/customers/:id
Update a customer: POST /v1/customers/:id with body
Delete a customer: DELETE /v1/customers/:id

What method does Stripe use to update?
POST
How is that different from my design?
uses POST for updating customers

## My conclusion
One thing I'd keep from my design: using PATCH for update method
One thing I'd change or reconsider: add /v1 to the start of every path so future breaking changes can go under /v2
