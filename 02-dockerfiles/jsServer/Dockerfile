FROM node:18

# Copy package.json and package-lock.json (if present) first for better layer caching
COPY package.json ./ 

# Install dependencies
RUN npm install

# Copy application code
COPY index.js ./
EXPOSE 3000
CMD ["npm", "start"]