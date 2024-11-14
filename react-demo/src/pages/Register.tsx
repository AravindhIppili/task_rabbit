import { useState } from "react";
import { PasswordInput } from "../components/ui/password-input";
import { Button, Container, Input, Text, VStack } from "@chakra-ui/react";
import axios, { AxiosError } from "axios";
import { base_url } from "../utils/config";
import { toaster } from "../components/ui/toaster";

export default function Register() {
  const [fullname, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [cnfpassword, setCnfPassword] = useState("");

  const handleSubmit = async () => {
    try {
      const data = {
        fullname: fullname,
        email: email,
        password: password,
        cnfpassword: cnfpassword,
      };
      const resp = await axios.post(`${base_url}/auth/register`, data);
      toaster.create({
        description: "Login successful",
        type: "success",
      });
    } catch (e) {
      toaster.create({
        description: String(e),
        type: "error",
      });
    }
  };

  return (
    <Container
      display="flex"
      justifyContent="center"
      alignItems="center"
      h="100%"
    >
      <VStack minW="400px">
        <Input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <Input
          type="text"
          placeholder="Full Name"
          value={fullname}
          onChange={(e) => setFullName(e.target.value)}
        />
        <PasswordInput
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Input
          type="text"
          placeholder="Confirm Password"
          value={cnfpassword}
          onChange={(e) => setCnfPassword(e.target.value)}
        />
        <Button onClick={handleSubmit}>
          <Text>Submit</Text>
        </Button>
      </VStack>
    </Container>
  );
}
