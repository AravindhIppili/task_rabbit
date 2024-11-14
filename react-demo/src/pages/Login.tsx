import { PasswordInput } from "../components/ui/password-input";
import { Button, Container, Input, Text, VStack } from "@chakra-ui/react";

export default function Login() {
  return (
    <Container>
      <VStack>
        <Input type="text" placeholder="Email" />
        <Input type="text" placeholder="Full Name" />
        <PasswordInput placeholder="Password" />
        <Input type="text" placeholder="Confirm Password" />
        <Button>
          <Text>Submit</Text>
        </Button>
      </VStack>
    </Container>
  );
}
