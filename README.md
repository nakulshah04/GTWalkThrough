# GTWalkThrough 🚧🗺️

**GTWalkThrough** is a community-powered web app designed to help Georgia Tech students and staff navigate campus more efficiently by avoiding active construction zones. Through an interactive map and smart rerouting features, users can plan safer, smoother commutes even during heavy campus construction periods.

## 🎯 Key Features

- **Interactive Campus Map**:
  - Displays real-time construction zones (entrances, sidewalks, roads).
  - Highlights blocked or rerouted paths clearly for easier navigation.
- **Community-Driven Reporting**:
  - Users can report newly created, completed, or shifted construction zones.
  - Report submission includes description and date information.
- **Smart Rerouting**:
  - Automatically suggests alternative paths to minimize delays and confusion.
- **Saved Routes** (upcoming):
  - Users will be able to save their preferred routes and get alerts if construction affects them.
- **Admin Controls**:
  - Admins can log in securely.
  - Approve or reject user-submitted construction reports.
  - Manually add, edit, or delete construction zones.
- **Password Reset System**:
  - Users can reset forgotten passwords via email verification and new password setup.

## 🛠️ Technologies Used

- **Backend**: Python (Django)
- **Frontend**: HTML5, CSS3 (Custom + Bootstrap elements)
- **Styling**:
  - Custom responsive styles using Roboto font.
  - Georgia Tech-inspired color palette (GT Blue and GT Gold).
- **Mapping and Navigation**: Google Maps JavaScript API
- **Authentication and Authorization**: Django's built-in system with enhancements (password reset workflow).
- **Deployment-Ready**: Modular and extensible project structure.

## 🔐 Environment Variables

To keep sensitive data secure, such as API keys, the project uses environment variables via a `.env` file. Before running the project locally, create a `.env` file in the root directory (same level as `manage.py`) and add the following: `GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here`. The key will be automatically loaded using `python-dotenv`. Be sure **not to commit** your `.env` file — it is already included in `.gitignore`. 

## 🖌️ UI/UX Enhancements

- Modern, consistent styling across login, register, and password reset pages.
- Hover effects and smooth transitions for navigation links.
- Responsive design for different screen sizes.
- Friendly user greeting after login using first name.
- Visually distinct form designs with accessible color contrasts.

## 📌 How To Use

1. **Users**:
   - Browse the map to view active construction zones.
   - Submit new construction zone reports if needed.
   - View suggested reroutes.
   - Reset password if needed via email-based recovery.

2. **Admins**:
   - Log in with admin credentials.
   - Approve, reject, or modify construction zone reports.
   - Manage the live construction map to ensure accuracy.

## 🚀 Future Enhancements

- Notifications for users when saved routes are impacted by new construction.
- Heatmaps to visualize areas with the highest construction activity.
- User profiles for managing saved routes and settings.
- Fully functional search bar for map and construction reports.
- Mobile app companion with real-time alerts and route rerouting.

## 📍 Built For

Students, faculty, and visitors at **Georgia Institute of Technology** seeking a smarter, safer, and faster way to walk through campus during periods of heavy construction.

## 📸 Screenshots (Coming Soon)

Visuals showcasing:
- Home Page with Interactive Map
- Construction Reporting Form
- Admin Dashboard
- Login and Registration Pages
