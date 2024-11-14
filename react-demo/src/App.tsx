import { RouterProvider } from "react-router-dom";
import router from "./AppRouter";
import { Provider } from "./components/ui/provider";
import { Toaster } from "./components/ui/toaster";

function App() {
  return (
    <Provider>
      <RouterProvider router={router} />;
      <Toaster />
    </Provider>
  );
}

export default App;
