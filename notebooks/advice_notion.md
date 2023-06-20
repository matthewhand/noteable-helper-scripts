# Advice for Working with Notion API

1. **Environment Variables**: When working from a Python notebook, you should set the `NOTION_API_KEY` environment variable with your Notion API key. If you're interacting with a specific database in Notion, you should also set the `NOTION_DATABASE_ID` environment variable with the ID of that database.

2. **Notion API Version**: When making requests to the Notion API, you need to include the 'Notion-Version' in the headers of your API request. As of June 28, 2022, the version should be set to '2022-06-28'. Here's a code fragment showing how to set the headers:

```python
# Headers for the API request
headers = {
 'Authorization': f'Bearer {NOTION_API_KEY}',
 'Notion-Version': '2022-06-28'
}
```

3. **Database Structure**: This guide assumes that each project is a page in the database, and that the page has a 'Name' property (the name of the project) and a 'Status' property (the status of the project). If your database is structured differently, you may need to adjust your scripts accordingly.
