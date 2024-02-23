## Python Django API Challenge with PostgreSQL Integration

### Challenge Description
This challenge combines problem-solving within the Django framework, HTTP API development with Django REST framework, and integration with a PostgreSQL database. Additionally, you will need to demonstrate proficiency in version control using Git by making appropriate commits and pull requests.

### Instructions
1. Fork the repository from the provided link.
2. Create a new branch
3. Set up a PostgreSQL database and configure the Django project to use it.
4. Create a simple database schema with one table to store items. The table should have at least the following columns:
   - `id` (primary key)
   - `name`
   - `description`
   - Add any additional columns you think are necessary.
5. Implement the HTTP API routes as described below, ensuring that they interact with the PostgreSQL database:
   - **GET `/api/items/`**: Retrieve a list of all items from the PostgreSQL database.
   - **POST `/api/items/`**: Create a new item and store it in the PostgreSQL database.
   - **PUT `/api/items/<item_id>/`**: Update an existing item identified by `<item_id>` in the PostgreSQL database.
6. Write tests for the API routes to ensure their correctness and the integration with the database.
7. Make commits as you progress, ensuring each commit has a clear and descriptive message.
8. Once you're confident in your solution, push your branch to your forked repository.
9. Open a pull request from your branch to the original repository's `main` branch.
10. Provide a brief explanation of your approach in the pull request description.

### Evaluation Criteria
- Correct implementation of CRUD operations for the HTTP API routes.
- Creation of a simple database schema and table structure in PostgreSQL.
- Integration of PostgreSQL database with Django models.
- Quality and clarity of code.
- Presence of descriptive commit messages.
- Completion of tests to ensure functionality.

### Resources
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### Deadline
24hs from received acknowledgement.

### Additional Notes
- Feel free to reach out if you have any questions or need clarification on the problem or instructions.
- Remember to adhere to best practices in coding, version control, and database integration throughout the process. Good luck!
